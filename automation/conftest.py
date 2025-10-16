"""
Pytest configuration and fixtures for Selenium tests.
"""

import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def base_url():
    """
    Fixture for base URL of the application.
    Can be overridden with environment variable.
    """
    return os.environ.get('BASE_URL', 'http://localhost:5000')


@pytest.fixture(scope='function')
def driver(request):
    """
    Fixture for Selenium WebDriver.
    Creates a new driver instance for each test.
    Automatically handles screenshots on failure.
    """
    # Set up Chrome options
    chrome_options = Options()
    
    # Check if running in CI or headless mode
    if os.environ.get('CI') or os.environ.get('HEADLESS'):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Additional options for stability
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-notifications')
    
    # Initialize Chrome driver with proper path
    try:
        driver_path = ChromeDriverManager().install()
        # Ensure we have the actual .exe file, not a directory or other file
        if not driver_path.endswith('.exe'):
            # Look for chromedriver.exe in the same directory
            import pathlib
            driver_dir = pathlib.Path(driver_path).parent
            driver_path = str(driver_dir / 'chromedriver.exe')
        
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        # Fallback: try without specifying service (use system PATH)
        print(f"ChromeDriver setup error: {e}")
        print("Attempting to use Chrome driver from system PATH...")
        driver = webdriver.Chrome(options=chrome_options)
    
    # Implicit wait
    driver.implicitly_wait(10)
    
    # Maximize window (if not headless)
    if not chrome_options.arguments.__contains__('--headless'):
        driver.maximize_window()
    
    # Yield driver to test
    yield driver
    
    # Teardown: Take screenshot on failure
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        take_screenshot(driver, request.node.name)
    
    # Close browser
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to access test result and make it available to fixtures.
    Used for taking screenshots on test failure.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def take_screenshot(driver, test_name):
    """
    Take screenshot and save to reports/screenshots directory.
    
    Args:
        driver: WebDriver instance
        test_name: Name of the test for filename
    """
    # Create screenshots directory if it doesn't exist
    screenshots_dir = os.path.join(os.path.dirname(__file__), 'reports', 'screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(screenshots_dir, filename)
    
    # Take screenshot
    driver.save_screenshot(filepath)
    print(f"\nScreenshot saved: {filepath}")


@pytest.fixture(scope='function')
def login_as_reporter(driver, base_url):
    """
    Fixture to login as reporter before test.
    
    Args:
        driver: WebDriver instance
        base_url: Base URL of application
    """
    login_page = LoginPage(driver, base_url)
    login_page.navigate_to_login()
    login_page.login('reporter@example.com', 'password123')


@pytest.fixture(scope='function')
def login_as_manager(driver, base_url):
    """
    Fixture to login as manager before test.
    
    Args:
        driver: WebDriver instance
        base_url: Base URL of application
    """
    login_page = LoginPage(driver, base_url)
    login_page.navigate_to_login()
    login_page.login('manager@example.com', 'password123')


# Pytest command line options
def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--base-url",
        action="store",
        default="http://localhost:5000",
        help="Base URL of the application"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )


# Configure markers
def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
    config.addinivalue_line("markers", "regression: mark test as regression test")
    config.addinivalue_line("markers", "login: mark test as login related")
    config.addinivalue_line("markers", "crud: mark test as CRUD operation test")
    config.addinivalue_line("markers", "permissions: mark test as permission related")
