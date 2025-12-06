"""
Flask Bug Tracker Application
A simple bug tracking system with user authentication and CRUD operations.
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from models import db, User, Bug
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugtracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BASE_PATH'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialize database
db.init_app(app)

# Register support chat blueprint
from support import support_bp
app.register_blueprint(support_bp)


def init_db():
    """Initialize database with mock users and sample bugs."""
    with app.app_context():
        db.create_all()
        
        # Check if users already exist
        if User.query.count() == 0:
            # Create mock users
            reporter = User(
                email='reporter@example.com',
                password='password123',  # In production, use hashed passwords
                role='reporter'
            )
            manager = User(
                email='manager@example.com',
                password='password123',
                role='manager'
            )
            
            db.session.add(reporter)
            db.session.add(manager)
            db.session.commit()
            
            # Create sample bugs
            sample_bugs = [
                Bug(
                    title='Login button not responding',
                    description='When clicking the login button, nothing happens on slow connections.',
                    severity='High',
                    status='Open',
                    reporter='reporter@example.com',
                    reporter_id=reporter.id
                ),
                Bug(
                    title='Dashboard loading slowly',
                    description='Dashboard takes more than 5 seconds to load with 100+ bugs.',
                    severity='Medium',
                    status='Open',
                    reporter='reporter@example.com',
                    reporter_id=reporter.id
                ),
                Bug(
                    title='Typo in header',
                    description='The header says "Bug Trakcer" instead of "Bug Tracker".',
                    severity='Low',
                    status='Closed',
                    reporter='manager@example.com',
                    reporter_id=manager.id
                )
            ]
            
            for bug in sample_bugs:
                db.session.add(bug)
            
            db.session.commit()
            print("Database initialized with mock data!")


@app.route('/')
def index():
    """Redirect to login page."""
    if 'user_email' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        
        # Validate input
        if not email or not password:
            flash('Email and password are required.', 'error')
            return render_template('login.html')
        
        # Check credentials
        user = User.query.filter_by(email=email, password=password).first()
        
        if user:
            session['user_email'] = user.email
            session['user_role'] = user.role
            session['user_id'] = user.id
            flash(f'Welcome, {user.email}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'error')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """Handle user logout."""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    """Display bug list with filtering options."""
    if 'user_email' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))
    
    # Get filter parameters
    status_filter = request.args.get('status', '')
    severity_filter = request.args.get('severity', '')
    
    # Build query
    query = Bug.query
    
    if status_filter:
        query = query.filter_by(status=status_filter)
    
    if severity_filter:
        query = query.filter_by(severity=severity_filter)
    
    bugs = query.order_by(Bug.created_date.desc()).all()
    
    return render_template('dashboard.html', 
                         bugs=bugs, 
                         user_email=session['user_email'],
                         user_role=session['user_role'],
                         status_filter=status_filter,
                         severity_filter=severity_filter)


@app.route('/bug/create', methods=['GET', 'POST'])
def create_bug():
    """Create a new bug."""
    if 'user_email' not in session:
        flash('Please log in to create a bug.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        severity = request.form.get('severity', '').strip()
        status = request.form.get('status', '').strip()
        
        # Server-side validation
        errors = []
        if not title:
            errors.append('Title is required.')
        if not description:
            errors.append('Description is required.')
        if severity not in ['Low', 'Medium', 'High']:
            errors.append('Invalid severity level.')
        if status not in ['Open', 'Closed']:
            errors.append('Invalid status.')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('bug_form.html', 
                                 title=title, 
                                 description=description,
                                 severity=severity,
                                 status=status,
                                 mode='create')
        
        # Create bug
        bug = Bug(
            title=title,
            description=description,
            severity=severity,
            status=status,
            reporter=session['user_email'],
            reporter_id=session['user_id']
        )
        
        db.session.add(bug)
        db.session.commit()
        
        flash('Bug created successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('bug_form.html', mode='create')


@app.route('/bug/edit/<int:bug_id>', methods=['GET', 'POST'])
def edit_bug(bug_id):
    """Edit an existing bug."""
    if 'user_email' not in session:
        flash('Please log in to edit a bug.', 'error')
        return redirect(url_for('login'))
    
    bug = Bug.query.get_or_404(bug_id)
    
    # Check permissions
    if session['user_role'] != 'manager' and bug.reporter_id != session['user_id']:
        flash('You do not have permission to edit this bug.', 'error')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        severity = request.form.get('severity', '').strip()
        status = request.form.get('status', '').strip()
        
        # Server-side validation
        errors = []
        if not title:
            errors.append('Title is required.')
        if not description:
            errors.append('Description is required.')
        if severity not in ['Low', 'Medium', 'High']:
            errors.append('Invalid severity level.')
        if status not in ['Open', 'Closed']:
            errors.append('Invalid status.')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('bug_form.html', 
                                 bug=bug, 
                                 mode='edit')
        
        # Update bug
        bug.title = title
        bug.description = description
        bug.severity = severity
        bug.status = status
        bug.updated_date = datetime.utcnow()
        
        db.session.commit()
        
        flash('Bug updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('bug_form.html', bug=bug, mode='edit')


@app.route('/bug/delete/<int:bug_id>', methods=['POST'])
def delete_bug(bug_id):
    """Delete a bug."""
    if 'user_email' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    bug = Bug.query.get_or_404(bug_id)
    
    # Check permissions
    if session['user_role'] != 'manager' and bug.reporter_id != session['user_id']:
        return jsonify({'success': False, 'message': 'Permission denied'}), 403
    
    db.session.delete(bug)
    db.session.commit()
    
    flash('Bug deleted successfully!', 'success')
    return jsonify({'success': True})


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
