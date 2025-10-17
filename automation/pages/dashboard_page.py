"""
Dashboard Page Object
Represents the dashboard/bug list page and its elements.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    """Page object for the dashboard page."""
    
    # Locators using data-test attributes
    DASHBOARD_TITLE = (By.CSS_SELECTOR, '[data-test="dashboard-title"]')
    USER_EMAIL = (By.CSS_SELECTOR, '[data-test="user-email"]')
    USER_ROLE = (By.CSS_SELECTOR, '[data-test="user-role"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="logout-button"]')
    CREATE_BUG_BUTTON = (By.CSS_SELECTOR, '[data-test="create-bug-button"]')
    
    # Filter elements
    FILTER_STATUS = (By.CSS_SELECTOR, '[data-test="filter-status"]')
    FILTER_SEVERITY = (By.CSS_SELECTOR, '[data-test="filter-severity"]')
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, '[data-test="apply-filter-button"]')
    CLEAR_FILTER_BUTTON = (By.CSS_SELECTOR, '[data-test="clear-filter-button"]')
    
    # Bug table
    BUG_TABLE = (By.CSS_SELECTOR, '[data-test="bug-table"]')
    NO_BUGS_MESSAGE = (By.CSS_SELECTOR, '[data-test="no-bugs-message"]')
    
    # Flash messages
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[data-test="flash-message-success"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="flash-message-error"]')
    
    def __init__(self, driver, base_url='http://localhost:5000'):
        """
        Initialize the dashboard page.
        
        Args:
            driver: WebDriver instance
            base_url: Base URL of the application
        """
        super().__init__(driver)
        self.base_url = base_url
        self.url = f"{base_url}/dashboard"
    
    def navigate_to_dashboard(self):
        """Navigate to the dashboard page."""
        self.driver.get(self.url)
    
    def is_on_dashboard(self):
        """
        Verify if currently on dashboard page.
        
        Returns:
            True if on dashboard, False otherwise
        """
        return self.is_element_visible(self.DASHBOARD_TITLE)
    
    def get_user_email(self):
        """
        Get the logged-in user's email.
        
        Returns:
            User email text
        """
        return self.get_text(self.USER_EMAIL)
    
    def get_user_role(self):
        """
        Get the logged-in user's role.
        
        Returns:
            User role text
        """
        return self.get_text(self.USER_ROLE)
    
    def click_logout(self):
        """Click the logout button."""
        self.click(self.LOGOUT_BUTTON)
    
    def click_create_bug(self):
        """Click the create bug button."""
        self.click(self.CREATE_BUG_BUTTON)
    
    def filter_by_status(self, status):
        """
        Filter bugs by status.
        
        Args:
            status: Status value ('Open' or 'Closed')
        """
        self.select_dropdown_by_value(self.FILTER_STATUS, status)
        self.click(self.APPLY_FILTER_BUTTON)
    
    def filter_by_severity(self, severity):
        """
        Filter bugs by severity.
        
        Args:
            severity: Severity value ('Low', 'Medium', or 'High')
        """
        self.select_dropdown_by_value(self.FILTER_SEVERITY, severity)
        self.click(self.APPLY_FILTER_BUTTON)
    
    def clear_filters(self):
        """Clear all applied filters."""
        self.click(self.CLEAR_FILTER_BUTTON)
    
    def is_bug_table_visible(self):
        """
        Check if bug table is visible.
        
        Returns:
            True if table is visible, False otherwise
        """
        return self.is_element_visible(self.BUG_TABLE, timeout=5)
    
    def is_no_bugs_message_visible(self):
        """
        Check if 'no bugs' message is visible.
        
        Returns:
            True if message is visible, False otherwise
        """
        return self.is_element_visible(self.NO_BUGS_MESSAGE, timeout=5)
    
    def get_bug_row(self, bug_id):
        """
        Get a specific bug row element.
        
        Args:
            bug_id: ID of the bug
            
        Returns:
            WebElement for the bug row
        """
        locator = (By.CSS_SELECTOR, f'[data-test="bug-row-{bug_id}"]')
        return self.find_element(locator)
    
    def get_bug_title(self, bug_id):
        """
        Get bug title from table.
        
        Args:
            bug_id: ID of the bug
            
        Returns:
            Bug title text
        """
        locator = (By.CSS_SELECTOR, f'[data-test="bug-title-{bug_id}"]')
        return self.get_text(locator)
    
    def get_bug_severity(self, bug_id):
        """
        Get bug severity from table.
        
        Args:
            bug_id: ID of the bug
            
        Returns:
            Bug severity text
        """
        locator = (By.CSS_SELECTOR, f'[data-test="bug-severity-{bug_id}"]')
        return self.get_text(locator)
    
    def get_bug_status(self, bug_id):
        """
        Get bug status from table.
        
        Args:
            bug_id: ID of the bug
            
        Returns:
            Bug status text
        """
        locator = (By.CSS_SELECTOR, f'[data-test="bug-status-{bug_id}"]')
        return self.get_text(locator)
    
    def click_edit_bug(self, bug_id):
        """
        Click edit button for a specific bug.
        
        Args:
            bug_id: ID of the bug
        """
        locator = (By.CSS_SELECTOR, f'[data-test="edit-bug-{bug_id}"]')
        self.click(locator)
    
    def click_delete_bug(self, bug_id):
        """
        Click delete button for a specific bug.
        
        Args:
            bug_id: ID of the bug
        """
        locator = (By.CSS_SELECTOR, f'[data-test="delete-bug-{bug_id}"]')
        # Ensure row and button are in view before clicking
        try:
            row = self.get_bug_row(bug_id)
            self.scroll_into_view(row)
        except Exception:
            pass
        self.click(locator)
        # Handle JavaScript confirm dialog with an explicit wait
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
    
    def is_edit_button_visible(self, bug_id):
        """
        Check if edit button is visible for a bug.
        
        Args:
            bug_id: ID of the bug
            
        Returns:
            True if button is visible, False otherwise
        """
        locator = (By.CSS_SELECTOR, f'[data-test="edit-bug-{bug_id}"]')
        return self.is_element_visible(locator, timeout=2)
    
    def is_delete_button_visible(self, bug_id):
        """
        Check if delete button is visible for a bug.
        
        Args:
            bug_id: ID of the bug
            
        Returns:
            True if button is visible, False otherwise
        """
        locator = (By.CSS_SELECTOR, f'[data-test="delete-bug-{bug_id}"]')
        return self.is_element_visible(locator, timeout=2)
    
    def is_no_permission_message_visible(self, bug_id):
        """
        Check if 'no permission' message is visible for a bug.
        
        Args:
            bug_id: ID of the bug
            
        Returns:
            True if message is visible, False otherwise
        """
        locator = (By.CSS_SELECTOR, f'[data-test="no-permission-{bug_id}"]')
        return self.is_element_visible(locator, timeout=2)
    
    def get_all_bug_rows(self):
        """
        Get all bug rows from the table.
        
        Returns:
            List of WebElements representing bug rows
        """
        locator = (By.CSS_SELECTOR, 'tr[data-test^="bug-row-"]')
        return self.find_elements(locator)
    
    def get_success_message(self):
        """
        Get success message text.
        
        Returns:
            Success message text
        """
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def is_success_message_displayed(self):
        """
        Check if success message is displayed.
        
        Returns:
            True if message is visible, False otherwise
        """
        return self.is_element_visible(self.SUCCESS_MESSAGE, timeout=5)
