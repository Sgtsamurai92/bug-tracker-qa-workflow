"""
Login Page Object
Represents the login page and its elements.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page."""
    
    # Locators using data-test attributes
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-test="email-input"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-test="password-input"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    LOGIN_TITLE = (By.CSS_SELECTOR, '[data-test="login-title"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="flash-message-error"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[data-test="flash-message-success"]')
    
    def __init__(self, driver, base_url='http://localhost:5000'):
        """
        Initialize the login page.
        
        Args:
            driver: WebDriver instance
            base_url: Base URL of the application
        """
        super().__init__(driver)
        self.base_url = base_url
        self.url = f"{base_url}/login"
    
    def navigate_to_login(self):
        """Navigate to the login page."""
        self.driver.get(self.url)
    
    def enter_email(self, email):
        """
        Enter email address.
        
        Args:
            email: Email address to enter
        """
        self.enter_text(self.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        """
        Enter password.
        
        Args:
            password: Password to enter
        """
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)
    
    def login(self, email, password):
        """
        Perform complete login action.
        
        Args:
            email: Email address
            password: Password
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
    
    def is_error_message_displayed(self):
        """
        Check if error message is displayed.
        
        Returns:
            True if error message is visible, False otherwise
        """
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=5)
    
    def get_error_message(self):
        """
        Get the error message text.
        
        Returns:
            Error message text
        """
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_success_message_displayed(self):
        """
        Check if success message is displayed.
        
        Returns:
            True if success message is visible, False otherwise
        """
        return self.is_element_visible(self.SUCCESS_MESSAGE, timeout=5)
    
    def is_on_login_page(self):
        """
        Verify if currently on login page.
        
        Returns:
            True if on login page, False otherwise
        """
        return self.is_element_visible(self.LOGIN_TITLE)
