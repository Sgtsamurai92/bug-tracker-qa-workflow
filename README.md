# 🐛 Bug Tracker QA Workflow# Bug Tracker QA Workflow (Manual → Automation → CI)



A comprehensive Quality Assurance portfolio project demonstrating a full testing workflow from requirements to automated CI/CD testing. This project includes a functional bug tracking web application and a complete Selenium-based test automation suite.A portfolio project that demonstrates a full QA workflow on a simple bug-tracker web app (or any demo bug tracker), including:

- Test planning & documentation

---- Manual testing with evidence

- Python Playwright automation with page objects

## 📋 Table of Contents- CI via GitHub Actions with artifacts (screenshots, videos, HTML report)



- [Project Overview](#project-overview)## How to Use This Repo

- [Features](#features)1. Review **TEST_PLAN.md** and **RTM.md** for scope and coverage.

- [Tech Stack](#tech-stack)2. See **/manual** for manual test cases, data, and evidence.

- [Quick Start](#quick-start)3. Run automation locally (below) or view CI logs & artifacts.

- [Running the Application](#running-the-application)

- [Running Tests](#running-tests)## Local Setup (Automation)

- [QA Documentation](#qa-documentation)```bash

- [CI/CD Pipeline](#cicd-pipeline)# Python 3.10+ recommended

python -m venv .venv

---source .venv/bin/activate  # Windows: .venv\Scripts\activate



## 🎯 Project Overviewpip install -r automation/requirements.txt



This project demonstrates a complete QA workflow:# run tests (headless by default; use HEADLESS=false to see browser)

pytest -q

1. **Requirements Documentation** - Clear feature specifications  # with HTML report:

2. **Test Planning** - Comprehensive test plan and strategy  pytest --html=automation/reports/report.html --self-contained-html
3. **Manual Test Cases** - Detailed test cases in CSV format  
4. **Test Automation** - Selenium WebDriver with Page Object Model  
5. **CI/CD Integration** - GitHub Actions for automated testing  
6. **Test Reporting** - HTML reports with screenshots on failure

---

## ✨ Features

### Bug Tracker Application
- 🔐 User authentication (Reporter/Manager roles)
- ✏️ Complete CRUD operations for bugs
- 🔍 Filter by status and severity
- 🔒 Role-based permissions
- 📱 Responsive Bootstrap UI

### Test Automation Suite
- 🏗️ Page Object Model architecture
- ✅ Pytest framework with fixtures
- 📸 Screenshot capture on failures
- 📊 HTML test reports
- 🤖 Headless execution for CI/CD

---

## 🛠️ Tech Stack

**Application:**
- Backend: Python 3.11+, Flask 3.0
- Database: SQLite
- Frontend: HTML5, CSS3, Bootstrap 5.3

**Testing:**
- Selenium 4.15+
- Pytest 7.4+
- WebDriver Manager

**CI/CD:**
- GitHub Actions

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Google Chrome browser
- Git

### Installation

```powershell
# Clone the repository
git clone https://github.com/yourusername/bug-tracker-qa-workflow.git
cd bug-tracker-qa-workflow

# Install Python dependencies
pip install -r automation/requirements.txt
```

---

## 🖥️ Running the Application

### Start Flask App

```powershell
cd app
python app.py
```

**Application URL:** http://localhost:5000

### Default Test Users

| Email | Password | Role |
|-------|----------|------|
| reporter@example.com | password123 | Reporter |
| manager@example.com | password123 | Manager |

### Sample Data
- 3 pre-seeded bugs (High, Medium, Low severity)
- 2 test user accounts

---

## 🧪 Running Tests

### Start Application First
```powershell
# Terminal 1: Start Flask app
cd app
python app.py
```

### Run Tests

```powershell
# Terminal 2: Run tests
cd automation
pytest tests/ -v
```

### Common Test Commands

**Run with HTML Report:**
```powershell
pytest tests/ --html=reports/report.html --self-contained-html -v
```

**Run Specific Test File:**
```powershell
pytest tests/test_login_valid_invalid.py -v
```

**Run in Headless Mode:**
```powershell
$env:HEADLESS="true"
pytest tests/ -v
```

**Run Tests in Parallel:**
```powershell
pytest tests/ -n 3 -v
```

---

## 📊 Test Reports

### View HTML Report

```powershell
start automation\reports\report.html
```

### Screenshots
Failed test screenshots are saved to:
```
automation/reports/screenshots/
```

Each screenshot includes:
- Test name
- Timestamp
- Browser state at failure

---

## 📚 QA Documentation

### Project Documentation Files

📄 **TEST_PLAN.md**
- Test strategy and objectives
- Scope and approach
- Environment setup
- Entry/exit criteria

📄 **RTM.md** (Requirements Traceability Matrix)
- Feature-to-test mapping
- Coverage analysis
- Traceability matrix

📄 **BUG_REPORT_TEMPLATE.md**
- Standard bug report format
- Severity levels
- Reproduction steps template

### Manual Testing Artifacts

📂 **manual/TestCases.csv**
- 25+ comprehensive test cases
- Test steps and expected results
- Priority and status tracking

📂 **manual/TestData.csv**
- Valid and invalid test data
- Edge cases and boundary values
- Security test data

📂 **manual/TestEvidence/**
- Screenshots and test evidence
- Manual test execution results

---

## 🔄 CI/CD Pipeline

### GitHub Actions Workflow

The project includes automated CI/CD that:

✅ Triggers on push/pull request  
✅ Sets up Python 3.11 environment  
✅ Installs all dependencies  
✅ Starts Flask application  
✅ Runs all tests in headless mode  
✅ Generates HTML reports  
✅ Uploads test artifacts  
✅ Captures failure screenshots  

### View CI Results

Check the **Actions** tab in GitHub to:
- View test execution status
- Download test reports
- View failure screenshots
- Track test trends

---

## 📁 Project Structure

```
bug-tracker-qa-workflow/
├── app/                          # Flask application
│   ├── app.py                    # Main application
│   ├── models.py                 # Database models
│   ├── templates/                # HTML templates
│   └── static/                   # CSS files
├── automation/                   # Test automation
│   ├── pages/                    # Page Objects
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── dashboard_page.py
│   │   └── bug_form_page.py
│   ├── tests/                    # Test cases
│   │   ├── test_login_valid_invalid.py
│   │   ├── test_bug_crud.py
│   │   └── test_filter_and_permissions.py
│   ├── reports/                  # Test reports
│   ├── conftest.py               # Pytest fixtures
│   ├── pytest.ini                # Configuration
│   └── requirements.txt          # Dependencies
├── manual/                       # Manual testing
│   ├── TestCases.csv
│   ├── TestData.csv
│   └── TestEvidence/
├── .github/workflows/            # CI/CD
│   └── ci.yml
├── TEST_PLAN.md
├── RTM.md
├── BUG_REPORT_TEMPLATE.md
└── README.md
```

---

## 🧑‍💻 Development Workflow

### Adding New Tests

1. Create test file in `automation/tests/`
2. Import page objects
3. Write test using pytest
4. Run locally to verify
5. Push and check CI execution

### Page Object Pattern

```python
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_example(driver, base_url):
    login_page = LoginPage(driver, base_url)
    dashboard_page = DashboardPage(driver, base_url)
    
    login_page.navigate_to_login()
    login_page.login('reporter@example.com', 'password123')
    
    assert dashboard_page.is_on_dashboard()
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue: ChromeDriver not found**
```powershell
pip install --upgrade webdriver-manager
```

**Issue: Flask port already in use**
```powershell
# Check what's using port 5000
netstat -ano | findstr :5000

# Kill the process if needed
Stop-Process -Id <PID>
```

**Issue: Tests timing out**
- Increase implicit wait in `conftest.py`
- Check if Flask app is running
- Verify BASE_URL is correct

**Issue: Import errors in tests**
```powershell
# Make sure you're in the automation directory
cd automation
pytest tests/ -v
```

---

## 📈 Test Coverage

### Current Test Suite

- ✅ **Login Tests** (7 tests)
  - Valid/invalid credentials
  - Empty field validation
  - Logout functionality

- ✅ **Bug CRUD Tests** (10 tests)
  - Create bugs (all severity levels)
  - Edit existing bugs
  - Required field validation
  - Status updates

- ✅ **Filter Tests** (6 tests)
  - Filter by status
  - Filter by severity
  - Clear filters

- ✅ **Permission Tests** (6 tests)
  - Reporter permissions
  - Manager permissions
  - Role-based access control

**Total: 29 automated test cases**

---

## 🎯 Best Practices Demonstrated

### QA Best Practices
✅ Comprehensive documentation  
✅ Manual and automated testing  
✅ Requirements traceability  
✅ Test data management  
✅ Risk-based prioritization  

### Automation Best Practices
✅ Page Object Model  
✅ Stable selectors (data-test)  
✅ Explicit waits  
✅ Screenshot on failure  
✅ CI/CD integration  
✅ Detailed reporting  

---

## 🚀 Future Enhancements

- [ ] API testing with requests
- [ ] Performance testing
- [ ] Database testing
- [ ] Visual regression testing
- [ ] Accessibility testing
- [ ] Cross-browser testing
- [ ] Mobile responsive testing

---

## 📝 Quick Reference

### Key Commands

```powershell
# Start application
cd app; python app.py

# Run all tests
cd automation; pytest tests/ -v

# Generate HTML report
pytest tests/ --html=reports/report.html --self-contained-html

# Run in headless mode
$env:HEADLESS="true"; pytest tests/ -v

# Run specific test
pytest tests/test_login_valid_invalid.py::TestLogin::test_valid_login_reporter -v
```

### Data-Test Attributes

All interactive elements use `data-test` attributes:
```html
<input data-test="email-input" />
<button data-test="login-button" />
<div data-test="bug-row-123" />
```

This ensures stable, maintainable test automation.

---

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Portfolio: [yourportfolio.com](https://yourportfolio.com)

---

## 📄 License

This project is created for educational and portfolio purposes.

---

## 🙏 Acknowledgments

This project demonstrates:
- ✨ Full-stack QA capabilities
- 🤖 Test automation expertise
- 🔄 CI/CD integration skills
- 📚 Professional QA documentation
- 🎯 Industry best practices

---

**Built with ❤️ for Quality Assurance**

*Last Updated: October 2025*
