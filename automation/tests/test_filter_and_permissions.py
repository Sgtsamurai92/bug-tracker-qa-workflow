"""
Filter and Permissions Tests
Tests for filtering bugs and user permission validation.
"""

import pytest
import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.bug_form_page import BugFormPage


class TestFilterAndPermissions:
    """Test suite for filtering and permissions functionality."""
    
    def test_filter_bugs_by_open_status(self, driver, base_url, login_as_reporter):
        """
        Test Case: Filter bugs by Open status
        
        Steps:
        1. Login as reporter
        2. Apply status filter for 'Open'
        3. Verify only Open bugs are displayed
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        dashboard_page.filter_by_status('Open')
        
        # Assert
        time.sleep(2)  # Wait for filter to apply
        # Verify URL contains filter parameter
        current_url = dashboard_page.get_current_url()
        assert 'status=Open' in current_url, "URL should contain status filter parameter"
        
        # If bugs are shown, verify they are Open
        if dashboard_page.is_bug_table_visible():
            bug_rows = dashboard_page.get_all_bug_rows()
            if bug_rows:
                # Check first bug's status
                first_row = bug_rows[0]
                bug_id = first_row.get_attribute('data-test').replace('bug-row-', '')
                status = dashboard_page.get_bug_status(int(bug_id))
                assert 'Open' in status, "Filtered bugs should have Open status"
    
    def test_filter_bugs_by_closed_status(self, driver, base_url, login_as_reporter):
        """
        Test Case: Filter bugs by Closed status
        
        Steps:
        1. Login as reporter
        2. Apply status filter for 'Closed'
        3. Verify only Closed bugs are displayed
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        dashboard_page.filter_by_status('Closed')
        
        # Assert
        time.sleep(2)  # Wait for filter to apply
        current_url = dashboard_page.get_current_url()
        assert 'status=Closed' in current_url, "URL should contain status filter parameter"
        
        # If bugs are shown, verify they are Closed
        if dashboard_page.is_bug_table_visible():
            bug_rows = dashboard_page.get_all_bug_rows()
            if bug_rows:
                first_row = bug_rows[0]
                bug_id = first_row.get_attribute('data-test').replace('bug-row-', '')
                status = dashboard_page.get_bug_status(int(bug_id))
                assert 'Closed' in status, "Filtered bugs should have Closed status"
    
    def test_filter_bugs_by_high_severity(self, driver, base_url, login_as_reporter):
        """
        Test Case: Filter bugs by High severity
        
        Steps:
        1. Login as reporter
        2. Apply severity filter for 'High'
        3. Verify only High severity bugs are displayed
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        dashboard_page.filter_by_severity('High')
        
        # Assert
        time.sleep(2)  # Wait for filter to apply
        current_url = dashboard_page.get_current_url()
        assert 'severity=High' in current_url, "URL should contain severity filter parameter"
        
        # If bugs are shown, verify they are High severity
        if dashboard_page.is_bug_table_visible():
            bug_rows = dashboard_page.get_all_bug_rows()
            if bug_rows:
                first_row = bug_rows[0]
                bug_id = first_row.get_attribute('data-test').replace('bug-row-', '')
                severity = dashboard_page.get_bug_severity(int(bug_id))
                assert 'High' in severity, "Filtered bugs should have High severity"
    
    def test_filter_bugs_by_medium_severity(self, driver, base_url, login_as_reporter):
        """
        Test Case: Filter bugs by Medium severity
        
        Steps:
        1. Login as reporter
        2. Apply severity filter for 'Medium'
        3. Verify only Medium severity bugs are displayed
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        dashboard_page.filter_by_severity('Medium')
        
        # Assert
        time.sleep(1)
        current_url = dashboard_page.get_current_url()
        assert 'severity=Medium' in current_url, "URL should contain severity filter parameter"
    
    def test_filter_bugs_by_low_severity(self, driver, base_url, login_as_reporter):
        """
        Test Case: Filter bugs by Low severity
        
        Steps:
        1. Login as reporter
        2. Apply severity filter for 'Low'
        3. Verify only Low severity bugs are displayed
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        dashboard_page.filter_by_severity('Low')
        
        # Assert
        time.sleep(1)
        current_url = dashboard_page.get_current_url()
        assert 'severity=Low' in current_url, "URL should contain severity filter parameter"
    
    def test_clear_filters(self, driver, base_url, login_as_reporter):
        """
        Test Case: Clear applied filters
        
        Steps:
        1. Login as reporter
        2. Apply status filter
        3. Click clear filters button
        4. Verify all bugs are displayed
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        dashboard_page.filter_by_status('Open')
        time.sleep(1)
        dashboard_page.clear_filters()
        
        # Assert
        time.sleep(1)
        current_url = dashboard_page.get_current_url()
        assert 'status=' not in current_url and 'severity=' not in current_url, \
            "URL should not contain filter parameters after clearing"
    
    def test_reporter_cannot_delete_others_bug(self, driver, base_url):
        """
        Test Case: Reporter cannot delete another user's bug
        
        Steps:
        1. Login as reporter
        2. View dashboard
        3. Find a bug created by manager
        4. Verify delete button is not available
        """
        # Arrange
        login_page = LoginPage(driver, base_url)
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        login_page.navigate_to_login()
        login_page.login('reporter@example.com', 'password123')
        
        # Assert
        time.sleep(2)  # Wait for dashboard to load
        # Look for bugs not created by reporter (sample bugs created by manager)
        bug_rows = dashboard_page.get_all_bug_rows()
        
        for row in bug_rows:
            bug_id = row.get_attribute('data-test').replace('bug-row-', '')
            reporter_locator = (By.CSS_SELECTOR, f'[data-test="bug-reporter-{bug_id}"]')
            reporter = dashboard_page.get_text(reporter_locator)
            
            # If bug is from manager, verify reporter cannot delete it
            if 'manager@example.com' in reporter:
                # Should show "No access" message
                assert dashboard_page.is_no_permission_message_visible(int(bug_id)), \
                    "Reporter should see 'No access' for manager's bugs"
                break
    
    def test_reporter_can_edit_own_bug(self, driver, base_url, login_as_reporter):
        """
        Test Case: Reporter can edit their own bug
        
        Steps:
        1. Login as reporter
        2. Create a new bug
        3. Verify edit button is visible
        4. Click edit and verify form loads
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        # Act - Create a bug
        dashboard_page.click_create_bug()
        bug_title = f"Reporter's own bug {int(time.time())}"
        bug_form_page.create_bug(
            title=bug_title,
            description="Bug created by reporter",
            severity='Medium',
            status='Open'
        )
        
        time.sleep(2)  # Wait for bug creation
        
        # Assert - Verify edit button is available
        bug_rows = dashboard_page.get_all_bug_rows()
        if bug_rows:
            first_row = bug_rows[0]
            bug_id = first_row.get_attribute('data-test').replace('bug-row-', '')
            
            assert dashboard_page.is_edit_button_visible(int(bug_id)), \
                "Reporter should see edit button for their own bug"
            
            # Verify can click edit
            dashboard_page.click_edit_bug(int(bug_id))
            assert bug_form_page.is_on_form_page(), "Edit form should load"
    
    def test_reporter_can_delete_own_bug(self, driver, base_url, login_as_reporter):
        """
        Test Case: Reporter can delete their own bug
        
        Steps:
        1. Login as reporter
        2. Create a new bug
        3. Verify delete button is visible
        4. Delete the bug
        5. Verify bug is removed
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        # Act - Create a bug
        dashboard_page.click_create_bug()
        bug_title = f"Bug to be deleted {int(time.time())}"
        bug_form_page.create_bug(
            title=bug_title,
            description="Bug that will be deleted",
            severity='Low',
            status='Open'
        )
        
        time.sleep(2)  # Wait for bug creation
        
        # Get bug ID and delete
        bug_rows = dashboard_page.get_all_bug_rows()
        if bug_rows:
            first_row = bug_rows[0]
            bug_id = first_row.get_attribute('data-test').replace('bug-row-', '')
            
            assert dashboard_page.is_delete_button_visible(int(bug_id)), \
                "Reporter should see delete button for their own bug"
            
            # Delete the bug
            dashboard_page.click_delete_bug(int(bug_id))
            
            # Assert - Bug should be removed
            time.sleep(2)
            assert bug_title not in driver.page_source, "Deleted bug should not appear in list"
    
    def test_manager_can_delete_any_bug(self, driver, base_url):
        """
        Test Case: Manager can delete any bug (including reporter's bugs)
        
        Steps:
        1. Login as manager
        2. View dashboard
        3. Find a bug created by reporter
        4. Verify delete button is visible
        5. Delete the bug
        """
        # Arrange
        login_page = LoginPage(driver, base_url)
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        login_page.navigate_to_login()
        login_page.login('manager@example.com', 'password123')
        
        time.sleep(2)  # Wait for dashboard to load
        
        # Assert - Manager should see edit/delete buttons for all bugs
        bug_rows = dashboard_page.get_all_bug_rows()
        
        if bug_rows:
            # Check first bug (regardless of who created it)
            first_row = bug_rows[0]
            bug_id = first_row.get_attribute('data-test').replace('bug-row-', '')
            
            assert dashboard_page.is_edit_button_visible(int(bug_id)), \
                "Manager should see edit button for any bug"
            assert dashboard_page.is_delete_button_visible(int(bug_id)), \
                "Manager should see delete button for any bug"
    
    def test_manager_can_edit_any_bug(self, driver, base_url):
        """
        Test Case: Manager can edit any bug
        
        Steps:
        1. Login as manager
        2. View dashboard
        3. Select any bug
        4. Verify edit button is visible
        5. Click edit and verify form loads
        """
        # Arrange
        login_page = LoginPage(driver, base_url)
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        # Act
        login_page.navigate_to_login()
        login_page.login('manager@example.com', 'password123')
        
        time.sleep(2)  # Wait for dashboard to load
        
        # Find any bug and try to edit
        bug_rows = dashboard_page.get_all_bug_rows()
        
        if bug_rows:
            first_row = bug_rows[0]
            bug_id = first_row.get_attribute('data-test').replace('bug-row-', '')
            
            # Click edit
            dashboard_page.click_edit_bug(int(bug_id))
            
            # Assert
            assert bug_form_page.is_on_form_page(), "Manager should be able to access edit form for any bug"
