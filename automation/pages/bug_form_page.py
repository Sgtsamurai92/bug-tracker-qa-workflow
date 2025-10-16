"""
Bug Form Page Object
Represents the create/edit bug form page and its elements.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class BugFormPage(BasePage):
    """Page object for the bug creation and editing form."""
    
    # Locators using data-test attributes
    FORM_TITLE = (By.CSS_SELECTOR, '[data-test="form-title"]')
    TITLE_INPUT = (By.CSS_SELECTOR, '[data-test="title-input"]')
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, '[data-test="description-input"]')
    SEVERITY_SELECT = (By.CSS_SELECTOR, '[data-test="severity-select"]')
    STATUS_SELECT = (By.CSS_SELECTOR, '[data-test="status-select"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-test="submit-button"]')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '[data-test="cancel-button"]')
    BACK_TO_DASHBOARD = (By.CSS_SELECTOR, '[data-test="back-to-dashboard"]')
    
    # Error messages
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="flash-message-error"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[data-test="flash-message-success"]')
    
    def __init__(self, driver, base_url='http://localhost:5000'):
        """
        Initialize the bug form page.
        
        Args:
            driver: WebDriver instance
            base_url: Base URL of the application
        """
        super().__init__(driver)
        self.base_url = base_url
        self.create_url = f"{base_url}/bug/create"
    
    def navigate_to_create_bug(self):
        """Navigate to the create bug page."""
        self.driver.get(self.create_url)
    
    def navigate_to_edit_bug(self, bug_id):
        """
        Navigate to the edit bug page.
        
        Args:
            bug_id: ID of the bug to edit
        """
        edit_url = f"{self.base_url}/bug/edit/{bug_id}"
        self.driver.get(edit_url)
    
    def is_on_form_page(self):
        """
        Verify if currently on form page.
        
        Returns:
            True if on form page, False otherwise
        """
        return self.is_element_visible(self.FORM_TITLE)
    
    def get_form_title(self):
        """
        Get the form title text.
        
        Returns:
            Form title text
        """
        return self.get_text(self.FORM_TITLE)
    
    def enter_title(self, title):
        """
        Enter bug title.
        
        Args:
            title: Bug title text
        """
        self.enter_text(self.TITLE_INPUT, title)
    
    def enter_description(self, description):
        """
        Enter bug description.
        
        Args:
            description: Bug description text
        """
        self.enter_text(self.DESCRIPTION_INPUT, description)
    
    def select_severity(self, severity):
        """
        Select bug severity.
        
        Args:
            severity: Severity value ('Low', 'Medium', or 'High')
        """
        self.select_dropdown_by_value(self.SEVERITY_SELECT, severity)
    
    def select_status(self, status):
        """
        Select bug status.
        
        Args:
            status: Status value ('Open' or 'Closed')
        """
        self.select_dropdown_by_value(self.STATUS_SELECT, status)
    
    def click_submit(self):
        """Click the submit button."""
        self.click(self.SUBMIT_BUTTON)
    
    def click_cancel(self):
        """Click the cancel button."""
        self.click(self.CANCEL_BUTTON)
    
    def click_back_to_dashboard(self):
        """Click the back to dashboard button."""
        self.click(self.BACK_TO_DASHBOARD)
    
    def create_bug(self, title, description, severity, status):
        """
        Fill out and submit the bug creation form.
        
        Args:
            title: Bug title
            description: Bug description
            severity: Bug severity
            status: Bug status
        """
        self.enter_title(title)
        self.enter_description(description)
        self.select_severity(severity)
        self.select_status(status)
        self.click_submit()
    
    def edit_bug(self, title=None, description=None, severity=None, status=None):
        """
        Update bug fields and submit.
        
        Args:
            title: New title (optional)
            description: New description (optional)
            severity: New severity (optional)
            status: New status (optional)
        """
        if title:
            self.enter_title(title)
        if description:
            self.enter_description(description)
        if severity:
            self.select_severity(severity)
        if status:
            self.select_status(status)
        self.click_submit()
    
    def get_title_value(self):
        """
        Get current value of title input.
        
        Returns:
            Title input value
        """
        return self.get_attribute(self.TITLE_INPUT, 'value')
    
    def get_description_value(self):
        """
        Get current value of description input.
        
        Returns:
            Description textarea value
        """
        element = self.find_element(self.DESCRIPTION_INPUT)
        return element.get_attribute('value')
    
    def is_error_message_displayed(self):
        """
        Check if error message is displayed.
        
        Returns:
            True if error message is visible, False otherwise
        """
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=5)
    
    def get_error_message(self):
        """
        Get error message text.
        
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
    
    def submit_empty_form(self):
        """Submit the form without filling any fields."""
        self.click_submit()
