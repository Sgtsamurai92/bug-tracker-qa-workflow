"""
Pytest configuration and fixtures for Selenium tests.
"""

import pytest
import os
from datetime import datetime
from selenium import webdriver
import tempfile
import shutil
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
    
    # Use a fresh temporary profile and suppress first-run UI
    temp_profile_dir = tempfile.mkdtemp(prefix="chrome-profile-")
    chrome_options.add_argument(f"--user-data-dir={temp_profile_dir}")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--disable-first-run-ui")
    chrome_options.add_argument("--incognito")
    
    # Disable password manager, leak detection, and related UI bubbles
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 0,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordLeakDetection,SafeBrowsingEnhancedProtection")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    # Check if running in CI or headless mode (only run headless when explicitly set)
    if os.environ.get('CI') or os.environ.get('HEADLESS') == 'true':
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Enable verbose logging for debugging
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--v=1')
    
    # Additional options for stability
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-infobars')
    
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
    
    # Set implicit wait for better stability
    driver.implicitly_wait(15)
    
    # Maximize window for better visibility
    try:
        driver.maximize_window()
    except:
        # Fallback if maximize fails
        driver.set_window_size(1920, 1080)
    
    # Yield driver to test
    yield driver
    
    # Teardown: Take screenshot on failure
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        take_screenshot(driver, request.node.name)
    
    # Close browser
    driver.quit()
    # Clean up the temporary Chrome profile directory
    try:
        shutil.rmtree(temp_profile_dir, ignore_errors=True)
    except Exception as _:
        pass


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
