"""
Database models for Bug Tracker application.
Defines User and Bug models with SQLAlchemy.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """User model for authentication and authorization."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'reporter' or 'manager'
    
    # Relationship to bugs created by this user
    bugs = db.relationship('Bug', backref='reporter_user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.email} ({self.role})>'


class Bug(db.Model):
    """Bug model for tracking bugs."""
    __tablename__ = 'bugs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(20), nullable=False)  # Low, Medium, High
    status = db.Column(db.String(20), nullable=False)  # Open, Closed
    reporter = db.Column(db.String(120), nullable=False)
    reporter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Bug {self.id}: {self.title}>'
    
    def to_dict(self):
        """Convert bug object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'severity': self.severity,
            'status': self.status,
            'reporter': self.reporter,
            'reporter_id': self.reporter_id,
            'created_date': self.created_date.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_date': self.updated_date.strftime('%Y-%m-%d %H:%M:%S')
        }
