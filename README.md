# Bug Tracker QA Workflow# 🐛 Bug Tracker QA Workflow# Bug Tracker QA Workflow (Manual → Automation → CI)



A comprehensive Quality Assurance portfolio project demonstrating a full testing workflow from requirements to automated CI/CD testing. This project includes a functional bug tracking web application and a complete Selenium-based test automation suite.



---A comprehensive Quality Assurance portfolio project demonstrating a full testing workflow from requirements to automated CI/CD testing. This project includes a functional bug tracking web application and a complete Selenium-based test automation suite.A portfolio project that demonstrates a full QA workflow on a simple bug-tracker web app (or any demo bug tracker), including:



## Table of Contents- Test planning & documentation



- [Project Overview](#project-overview)---- Manual testing with evidence

- [Features](#features)

- [Tech Stack](#tech-stack)- Python Playwright automation with page objects

- [Quick Start](#quick-start)

- [Running the Application](#running-the-application)## 📋 Table of Contents- CI via GitHub Actions with artifacts (screenshots, videos, HTML report)

- [Running Tests](#running-tests)

- [QA Documentation](#qa-documentation)

- [CI/CD Pipeline](#cicd-pipeline)

- [Project Overview](#project-overview)## How to Use This Repo

---

- [Features](#features)1. Review **TEST_PLAN.md** and **RTM.md** for scope and coverage.

## Project Overview

- [Tech Stack](#tech-stack)2. See **/manual** for manual test cases, data, and evidence.

This project demonstrates a complete QA workflow:

- [Quick Start](#quick-start)3. Run automation locally (below) or view CI logs & artifacts.

1. **Requirements Documentation** - Clear feature specifications  

2. **Test Planning** - Comprehensive test plan and strategy  - [Running the Application](#running-the-application)

3. **Manual Test Cases** - Detailed test cases in CSV format  

4. **Test Automation** - Selenium WebDriver with Page Object Model  - [Running Tests](#running-tests)## Local Setup (Automation)

5. **CI/CD Integration** - GitHub Actions for automated testing  

6. **Test Reporting** - HTML reports with screenshots on failure- [QA Documentation](#qa-documentation)```bash



---- [CI/CD Pipeline](#cicd-pipeline)# Python 3.10+ recommended



## Featurespython -m venv .venv



### Bug Tracker Application---source .venv/bin/activate  # Windows: .venv\Scripts\activate

- User authentication (Reporter/Manager roles)

- Complete CRUD operations for bugs

- Filter by status and severity

- Role-based permissions## 🎯 Project Overviewpip install -r automation/requirements.txt

- Responsive Bootstrap UI



### Test Automation Suite

- Page Object Model architectureThis project demonstrates a complete QA workflow:# run tests (headless by default; use HEADLESS=false to see browser)

- Pytest framework with fixtures

- Screenshot capture on failurespytest -q

- HTML test reports

- Headless execution for CI/CD1. **Requirements Documentation** - Clear feature specifications  # with HTML report:



---2. **Test Planning** - Comprehensive test plan and strategy  pytest --html=automation/reports/report.html --self-contained-html

3. **Manual Test Cases** - Detailed test cases in CSV format  

## Tech Stack4. **Test Automation** - Selenium WebDriver with Page Object Model  

5. **CI/CD Integration** - GitHub Actions for automated testing  

**Application:**6. **Test Reporting** - HTML reports with screenshots on failure

- Backend: Python 3.11+, Flask 3.0

- Database: SQLite---

- Frontend: HTML5, CSS3, Bootstrap 5.3

## ✨ Features

**Testing:**

- Selenium 4.15+### Bug Tracker Application

- Pytest 7.4+- 🔐 User authentication (Reporter/Manager roles)

- WebDriver Manager- ✏️ Complete CRUD operations for bugs

- 🔍 Filter by status and severity

**CI/CD:**- 🔒 Role-based permissions

- GitHub Actions- 📱 Responsive Bootstrap UI



---### Test Automation Suite

- 🏗️ Page Object Model architecture

## Quick Start- ✅ Pytest framework with fixtures

- 📸 Screenshot capture on failures

### Prerequisites- 📊 HTML test reports

- Python 3.11 or higher- 🤖 Headless execution for CI/CD

- Google Chrome browser

- Git---



### Installation## 🛠️ Tech Stack



```powershell**Application:**

# Clone the repository- Backend: Python 3.11+, Flask 3.0

git clone https://github.com/Sgtsamurai92/bug-tracker-qa-workflow.git- Database: SQLite

cd bug-tracker-qa-workflow- Frontend: HTML5, CSS3, Bootstrap 5.3



# Install Python dependencies**Testing:**

pip install -r automation/requirements.txt- Selenium 4.15+

```- Pytest 7.4+

- WebDriver Manager

---

**CI/CD:**

## Running the Application- GitHub Actions



### Start Flask App---



```powershell## 🚀 Quick Start

cd app

python app.py### Prerequisites

```- Python 3.11 or higher

- Google Chrome browser

**Application URL:** http://localhost:5000- Git



### Default Test Users### Installation



| Email | Password | Role |```powershell

|-------|----------|------|# Clone the repository

| reporter@example.com | password123 | Reporter |git clone https://github.com/yourusername/bug-tracker-qa-workflow.git

| manager@example.com | password123 | Manager |cd bug-tracker-qa-workflow



### Sample Data# Install Python dependencies

- 3 pre-seeded bugs (High, Medium, Low severity)pip install -r automation/requirements.txt

- 2 test user accounts```



------



## Running Tests## 🖥️ Running the Application



### IMPORTANT: Start Application First### Start Flask App



The Flask application MUST be running before executing tests.```powershell

cd app

**Terminal 1: Start Flask App**python app.py

```powershell```

cd app

python app.py**Application URL:** http://localhost:5000

```

Keep this running!### Default Test Users



**Terminal 2: Run Tests**| Email | Password | Role |

```powershell|-------|----------|------|

cd automation| reporter@example.com | password123 | Reporter |

pytest tests/ -v| manager@example.com | password123 | Manager |

```

### Sample Data

### Common Test Commands- 3 pre-seeded bugs (High, Medium, Low severity)

- 2 test user accounts

**Run with HTML Report:**

```powershell---

pytest tests/ --html=reports/report.html --self-contained-html -v

```## 🧪 Running Tests



**Run Specific Test File:**### Start Application First

```powershell```powershell

pytest tests/test_login_valid_invalid.py -v# Terminal 1: Start Flask app

```cd app

python app.py

**Run in Headless Mode (Browser Hidden):**```

```powershell

$env:HEADLESS="true"### Run Tests

pytest tests/ -v

``````powershell

# Terminal 2: Run tests

**Run with Browser Visible (Default):**cd automation

```powershellpytest tests/ -v

# Just run without HEADLESS environment variable```

pytest tests/ -v

```### Common Test Commands



**Run Tests in Parallel:****Run with HTML Report:**

```powershell```powershell

pytest tests/ -n 3 -vpytest tests/ --html=reports/report.html --self-contained-html -v

``````



---**Run Specific Test File:**

```powershell

## Test Reportspytest tests/test_login_valid_invalid.py -v

```

### View HTML Report

**Run in Headless Mode:**

```powershell```powershell

start automation\reports\report.html$env:HEADLESS="true"

```pytest tests/ -v

```

### Screenshots

Failed test screenshots are saved to:**Run Tests in Parallel:**

``````powershell

automation/reports/screenshots/pytest tests/ -n 3 -v

``````



Each screenshot includes:---

- Test name

- Timestamp## 📊 Test Reports

- Browser state at failure

### View HTML Report

---

```powershell

## QA Documentationstart automation\reports\report.html

```

### Project Documentation Files

### Screenshots

**TEST_PLAN.md**Failed test screenshots are saved to:

- Test strategy and objectives```

- Scope and approachautomation/reports/screenshots/

- Environment setup```

- Entry/exit criteria

Each screenshot includes:

**RTM.md** (Requirements Traceability Matrix)- Test name

- Feature-to-test mapping- Timestamp

- Coverage analysis- Browser state at failure

- Traceability matrix

---

**BUG_REPORT_TEMPLATE.md**

- Standard bug report format## 📚 QA Documentation

- Severity levels

- Reproduction steps template### Project Documentation Files



### Manual Testing Artifacts📄 **TEST_PLAN.md**

- Test strategy and objectives

**manual/TestCases.csv**- Scope and approach

- 25+ comprehensive test cases- Environment setup

- Test steps and expected results- Entry/exit criteria

- Priority and status tracking

📄 **RTM.md** (Requirements Traceability Matrix)

**manual/TestData.csv**- Feature-to-test mapping

- Valid and invalid test data- Coverage analysis

- Edge cases and boundary values- Traceability matrix

- Security test data

📄 **BUG_REPORT_TEMPLATE.md**

**manual/TestEvidence/**- Standard bug report format

- Screenshots and test evidence- Severity levels

- Manual test execution results- Reproduction steps template



---### Manual Testing Artifacts



## CI/CD Pipeline📂 **manual/TestCases.csv**

- 25+ comprehensive test cases

### GitHub Actions Workflow- Test steps and expected results

- Priority and status tracking

The project includes automated CI/CD that:

📂 **manual/TestData.csv**

- Triggers on push/pull request  - Valid and invalid test data

- Sets up Python 3.11 environment  - Edge cases and boundary values

- Installs all dependencies  - Security test data

- Starts Flask application  

- Runs all tests in headless mode  📂 **manual/TestEvidence/**

- Generates HTML reports  - Screenshots and test evidence

- Uploads test artifacts  - Manual test execution results

- Captures failure screenshots  

---

### View CI Results

## 🔄 CI/CD Pipeline

Check the **Actions** tab in GitHub to:

- View test execution status### GitHub Actions Workflow

- Download test reports

- View failure screenshotsThe project includes automated CI/CD that:

- Track test trends

✅ Triggers on push/pull request  

---✅ Sets up Python 3.11 environment  

✅ Installs all dependencies  

## Project Structure✅ Starts Flask application  

✅ Runs all tests in headless mode  

```✅ Generates HTML reports  

bug-tracker-qa-workflow/✅ Uploads test artifacts  

├── app/                          # Flask application✅ Captures failure screenshots  

│   ├── app.py                    # Main application

│   ├── models.py                 # Database models### View CI Results

│   ├── templates/                # HTML templates

│   └── static/                   # CSS filesCheck the **Actions** tab in GitHub to:

├── automation/                   # Test automation- View test execution status

│   ├── pages/                    # Page Objects- Download test reports

│   │   ├── base_page.py- View failure screenshots

│   │   ├── login_page.py- Track test trends

│   │   ├── dashboard_page.py

│   │   └── bug_form_page.py---

│   ├── tests/                    # Test cases

│   │   ├── test_login_valid_invalid.py## 📁 Project Structure

│   │   ├── test_bug_crud.py

│   │   └── test_filter_and_permissions.py```

│   ├── reports/                  # Test reportsbug-tracker-qa-workflow/

│   ├── conftest.py               # Pytest fixtures├── app/                          # Flask application

│   ├── pytest.ini                # Configuration│   ├── app.py                    # Main application

│   └── requirements.txt          # Dependencies│   ├── models.py                 # Database models

├── manual/                       # Manual testing│   ├── templates/                # HTML templates

│   ├── TestCases.csv│   └── static/                   # CSS files

│   ├── TestData.csv├── automation/                   # Test automation

│   └── TestEvidence/│   ├── pages/                    # Page Objects

├── .github/workflows/            # CI/CD│   │   ├── base_page.py

│   └── ci.yml│   │   ├── login_page.py

├── TEST_PLAN.md│   │   ├── dashboard_page.py

├── RTM.md│   │   └── bug_form_page.py

├── BUG_REPORT_TEMPLATE.md│   ├── tests/                    # Test cases

└── README.md│   │   ├── test_login_valid_invalid.py

```│   │   ├── test_bug_crud.py

│   │   └── test_filter_and_permissions.py

---│   ├── reports/                  # Test reports

│   ├── conftest.py               # Pytest fixtures

## Development Workflow│   ├── pytest.ini                # Configuration

│   └── requirements.txt          # Dependencies

### Adding New Tests├── manual/                       # Manual testing

│   ├── TestCases.csv

1. Create test file in `automation/tests/`│   ├── TestData.csv

2. Import page objects│   └── TestEvidence/

3. Write test using pytest├── .github/workflows/            # CI/CD

4. Run locally to verify│   └── ci.yml

5. Push and check CI execution├── TEST_PLAN.md

├── RTM.md

### Page Object Pattern Example├── BUG_REPORT_TEMPLATE.md

└── README.md

```python```

from pages.login_page import LoginPage

from pages.dashboard_page import DashboardPage---



def test_example(driver, base_url):## 🧑‍💻 Development Workflow

    login_page = LoginPage(driver, base_url)

    dashboard_page = DashboardPage(driver, base_url)### Adding New Tests

    

    login_page.navigate_to_login()1. Create test file in `automation/tests/`

    login_page.login('reporter@example.com', 'password123')2. Import page objects

    3. Write test using pytest

    assert dashboard_page.is_on_dashboard()4. Run locally to verify

```5. Push and check CI execution



---### Page Object Pattern



## Troubleshooting```python

from pages.login_page import LoginPage

### Common Issuesfrom pages.dashboard_page import DashboardPage



**Issue: ChromeDriver not found**def test_example(driver, base_url):

```powershell    login_page = LoginPage(driver, base_url)

pip install --upgrade webdriver-manager    dashboard_page = DashboardPage(driver, base_url)

```    

    login_page.navigate_to_login()

**Issue: Flask port already in use**    login_page.login('reporter@example.com', 'password123')

```powershell    

# Check what's using port 5000    assert dashboard_page.is_on_dashboard()

netstat -ano | findstr :5000```



# Kill the process if needed---

Stop-Process -Id <PID>

```## 🐛 Troubleshooting



**Issue: Tests failing with connection refused**### Common Issues

- Make sure Flask app is running on http://localhost:5000

- Check if port 5000 is accessible**Issue: ChromeDriver not found**

- Verify no firewall blocking```powershell

pip install --upgrade webdriver-manager

**Issue: Tests timing out**```

- Increase implicit wait in `conftest.py`

- Check if Flask app is running**Issue: Flask port already in use**

- Verify BASE_URL is correct```powershell

# Check what's using port 5000

**Issue: Import errors in tests**netstat -ano | findstr :5000

```powershell

# Make sure you're in the automation directory# Kill the process if needed

cd automationStop-Process -Id <PID>

pytest tests/ -v```

```

**Issue: Tests timing out**

---- Increase implicit wait in `conftest.py`

- Check if Flask app is running

## Test Coverage- Verify BASE_URL is correct



### Current Test Suite**Issue: Import errors in tests**

```powershell

**Login Tests** (7 tests)# Make sure you're in the automation directory

- Valid/invalid credentialscd automation

- Empty field validationpytest tests/ -v

- Logout functionality```



**Bug CRUD Tests** (10 tests)---

- Create bugs (all severity levels)

- Edit existing bugs## 📈 Test Coverage

- Required field validation

- Status updates### Current Test Suite



**Filter Tests** (6 tests)- ✅ **Login Tests** (7 tests)

- Filter by status  - Valid/invalid credentials

- Filter by severity  - Empty field validation

- Clear filters  - Logout functionality



**Permission Tests** (6 tests)- ✅ **Bug CRUD Tests** (10 tests)

- Reporter permissions  - Create bugs (all severity levels)

- Manager permissions  - Edit existing bugs

- Role-based access control  - Required field validation

  - Status updates

**Total: 29 automated test cases**

- ✅ **Filter Tests** (6 tests)

---  - Filter by status

  - Filter by severity

## Best Practices Demonstrated  - Clear filters



### QA Best Practices- ✅ **Permission Tests** (6 tests)

- Comprehensive documentation    - Reporter permissions

- Manual and automated testing    - Manager permissions

- Requirements traceability    - Role-based access control

- Test data management  

- Risk-based prioritization  **Total: 29 automated test cases**



### Automation Best Practices---

- Page Object Model  

- Stable selectors (data-test)  ## 🎯 Best Practices Demonstrated

- Explicit waits  

- Screenshot on failure  ### QA Best Practices

- CI/CD integration  ✅ Comprehensive documentation  

- Detailed reporting  ✅ Manual and automated testing  

✅ Requirements traceability  

---✅ Test data management  

✅ Risk-based prioritization  

## Future Enhancements

### Automation Best Practices

- Add API testing with requests✅ Page Object Model  

- Implement performance testing✅ Stable selectors (data-test)  

- Add database testing✅ Explicit waits  

- Implement visual regression testing✅ Screenshot on failure  

- Add accessibility testing✅ CI/CD integration  

- Cross-browser testing✅ Detailed reporting  

- Mobile responsive testing

---

---

## 🚀 Future Enhancements

## Quick Reference

- [ ] API testing with requests

### Key Commands- [ ] Performance testing

- [ ] Database testing

```powershell- [ ] Visual regression testing

# Start application- [ ] Accessibility testing

cd app; python app.py- [ ] Cross-browser testing

- [ ] Mobile responsive testing

# Run all tests

cd automation; pytest tests/ -v---



# Generate HTML report## 📝 Quick Reference

pytest tests/ --html=reports/report.html --self-contained-html

### Key Commands

# Run in headless mode

$env:HEADLESS="true"; pytest tests/ -v```powershell

# Start application

# Run specific testcd app; python app.py

pytest tests/test_login_valid_invalid.py::TestLogin::test_valid_login_reporter -v

```# Run all tests

cd automation; pytest tests/ -v

### Data-Test Attributes

# Generate HTML report

All interactive elements use `data-test` attributes:pytest tests/ --html=reports/report.html --self-contained-html

```html

<input data-test="email-input" /># Run in headless mode

<button data-test="login-button" />$env:HEADLESS="true"; pytest tests/ -v

<div data-test="bug-row-123" />

```# Run specific test

pytest tests/test_login_valid_invalid.py::TestLogin::test_valid_login_reporter -v

This ensures stable, maintainable test automation.```



---### Data-Test Attributes



## AuthorAll interactive elements use `data-test` attributes:

```html

**Sgtsamurai92**<input data-test="email-input" />

- GitHub: [@Sgtsamurai92](https://github.com/Sgtsamurai92)<button data-test="login-button" />

- Repository: [bug-tracker-qa-workflow](https://github.com/Sgtsamurai92/bug-tracker-qa-workflow)<div data-test="bug-row-123" />

```

---

This ensures stable, maintainable test automation.

## License

---

This project is created for educational and portfolio purposes.

## 👤 Author

---

**Your Name**

## Acknowledgments- GitHub: [@yourusername](https://github.com/yourusername)

- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

This project demonstrates:- Portfolio: [yourportfolio.com](https://yourportfolio.com)

- Full-stack QA capabilities

- Test automation expertise---

- CI/CD integration skills

- Professional QA documentation## 📄 License

- Industry best practices

This project is created for educational and portfolio purposes.

---

---

**Built for Quality Assurance Excellence**

## 🙏 Acknowledgments

*Last Updated: October 2025*

This project demonstrates:
- ✨ Full-stack QA capabilities
- 🤖 Test automation expertise
- 🔄 CI/CD integration skills
- 📚 Professional QA documentation
- 🎯 Industry best practices

---

**Built with ❤️ for Quality Assurance**

*Last Updated: October 2025*
