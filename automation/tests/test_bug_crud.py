"""
Bug CRUD Tests
Tests for creating, reading, updating bugs with validation.
"""

import pytest
import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.bug_form_page import BugFormPage


class TestBugCRUD:
    """Test suite for bug CRUD operations."""
    
    def test_create_new_bug_success(self, driver, base_url, login_as_reporter):
        """
        Test Case: Successfully create a new bug
        
        Steps:
        1. Login as reporter
        2. Navigate to create bug page
        3. Fill in all required fields
        4. Submit the form
        5. Verify success message
        6. Verify bug appears in dashboard
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        bug_title = f"Test Bug {int(time.time())}"
        bug_description = "This is a test bug description for automation testing"
        
        # Act
        dashboard_page.click_create_bug()
        bug_form_page.create_bug(
            title=bug_title,
            description=bug_description,
            severity='High',
            status='Open'
        )
        
        # Assert
        assert dashboard_page.is_on_dashboard(), "Should redirect to dashboard after creation"
        assert dashboard_page.is_success_message_displayed(), "Success message should be displayed"
        
        # Verify bug appears in the list (check if title exists in page source)
        time.sleep(2)  # Wait for page to fully update
        assert bug_title in driver.page_source, "New bug should appear in the dashboard"
    
    def test_create_bug_with_all_severity_levels(self, driver, base_url, login_as_reporter):
        """
        Test Case: Create bugs with different severity levels
        
        Steps:
        1. Login as reporter
        2. Create bug with Low severity
        3. Create bug with Medium severity
        4. Create bug with High severity
        5. Verify all bugs are created
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        severities = ['Low', 'Medium', 'High']
        
        for severity in severities:
            # Act
            dashboard_page.click_create_bug()
            bug_title = f"Bug with {severity} severity {int(time.time())}"
            bug_form_page.create_bug(
                title=bug_title,
                description=f"Testing {severity} severity bug creation",
                severity=severity,
                status='Open'
            )
            
            # Assert
            time.sleep(1)
            assert bug_title in driver.page_source, f"Bug with {severity} severity should be created"
    
    def test_edit_existing_bug(self, driver, base_url, login_as_reporter):
        """
        Test Case: Edit an existing bug
        
        Steps:
        1. Login as reporter
        2. Create a new bug
        3. Edit the bug
        4. Verify changes are saved
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        original_title = f"Original Bug {int(time.time())}"
        updated_title = f"Updated Bug {int(time.time())}"
        
        # Act - Create bug
        dashboard_page.click_create_bug()
        bug_form_page.create_bug(
            title=original_title,
            description="Original description",
            severity='Low',
            status='Open'
        )
        
        time.sleep(2)  # Wait for creation to complete
        
        # Find and edit the bug - use the first available edit button
        # Since we just created it, it should be visible
        bug_rows = dashboard_page.get_all_bug_rows()
        if bug_rows:
            # Get the bug ID from the first row's data-test attribute
            first_row = bug_rows[0]
            bug_id = first_row.get_attribute('data-test').replace('bug-row-', '')
            
            dashboard_page.click_edit_bug(int(bug_id))
            time.sleep(1)  # Wait for form to load
            bug_form_page.edit_bug(
                title=updated_title,
                description="Updated description",
                severity='High',
                status='Closed'
            )
            
            # Assert
            time.sleep(1)
            assert dashboard_page.is_on_dashboard(), "Should be on dashboard after edit"
            assert dashboard_page.is_success_message_displayed(), "Success message should be displayed"
            assert updated_title in driver.page_source, "Updated bug title should appear"
    
    def test_create_bug_required_field_validation_title(self, driver, base_url, login_as_reporter):
        """
        Test Case: Validation error when title is missing
        
        Steps:
        1. Login as reporter
        2. Navigate to create bug page
        3. Leave title empty
        4. Fill other fields
        5. Submit form
        6. Verify validation error for title
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        # Act
        dashboard_page.click_create_bug()
        bug_form_page.enter_description("Description without title")
        bug_form_page.select_severity('Medium')
        bug_form_page.select_status('Open')
        bug_form_page.click_submit()
        
        # Assert
        # HTML5 validation should prevent submission
        assert bug_form_page.is_on_form_page(), "Should remain on form page with validation error"
    
    def test_create_bug_required_field_validation_description(self, driver, base_url, login_as_reporter):
        """
        Test Case: Validation error when description is missing
        
        Steps:
        1. Login as reporter
        2. Navigate to create bug page
        3. Leave description empty
        4. Fill other fields
        5. Submit form
        6. Verify validation error for description
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        # Act
        dashboard_page.click_create_bug()
        bug_form_page.enter_title(f"Title without description {int(time.time())}")
        bug_form_page.select_severity('Medium')
        bug_form_page.select_status('Open')
        # Clear description if any default value
        bug_form_page.enter_description('')
        bug_form_page.click_submit()
        
        # Assert
        # HTML5 validation should prevent submission
        assert bug_form_page.is_on_form_page(), "Should remain on form page with validation error"
    
    def test_create_bug_without_severity(self, driver, base_url, login_as_reporter):
        """
        Test Case: Validation error when severity is not selected
        
        Steps:
        1. Login as reporter
        2. Navigate to create bug page
        3. Fill title and description
        4. Leave severity unselected
        5. Submit form
        6. Verify validation error
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        # Act
        dashboard_page.click_create_bug()
        bug_form_page.enter_title(f"Bug without severity {int(time.time())}")
        bug_form_page.enter_description("Description for bug without severity")
        # Don't select severity
        bug_form_page.select_status('Open')
        bug_form_page.click_submit()
        
        # Assert
        # Should show server-side validation error or HTML5 validation
        assert bug_form_page.is_on_form_page(), "Should remain on form page"
    
    def test_cancel_bug_creation(self, driver, base_url, login_as_reporter):
        """
        Test Case: Cancel bug creation
        
        Steps:
        1. Login as reporter
        2. Navigate to create bug page
        3. Fill in some fields
        4. Click cancel button
        5. Verify user returns to dashboard
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        # Act
        dashboard_page.click_create_bug()
        bug_form_page.enter_title("Bug to be cancelled")
        bug_form_page.click_cancel()
        
        # Assert
        assert dashboard_page.is_on_dashboard(), "Should return to dashboard after cancel"
    
    def test_bug_status_update(self, driver, base_url, login_as_reporter):
        """
        Test Case: Update bug status from Open to Closed
        
        Steps:
        1. Login as reporter
        2. Create a bug with Open status
        3. Edit bug and change status to Closed
        4. Verify status is updated
        """
        # Arrange
        dashboard_page = DashboardPage(driver, base_url)
        bug_form_page = BugFormPage(driver, base_url)
        
        bug_title = f"Bug for status update {int(time.time())}"
        
        # Act - Create bug with Open status
        dashboard_page.click_create_bug()
        bug_form_page.create_bug(
            title=bug_title,
            description="Bug to test status update",
            severity='Medium',
            status='Open'
        )
        
        time.sleep(1)
        
        # Edit and change status
        bug_rows = dashboard_page.get_all_bug_rows()
        if bug_rows:
            first_row = bug_rows[0]
            bug_id = first_row.get_attribute('data-test').replace('bug-row-', '')
            
            dashboard_page.click_edit_bug(int(bug_id))
            bug_form_page.select_status('Closed')
            bug_form_page.click_submit()
            
            # Assert
            time.sleep(1)
            assert dashboard_page.is_on_dashboard(), "Should be on dashboard"
            # Verify the bug shows Closed status
            status_text = dashboard_page.get_bug_status(int(bug_id))
            assert 'Closed' in status_text, "Bug status should be updated to Closed"
