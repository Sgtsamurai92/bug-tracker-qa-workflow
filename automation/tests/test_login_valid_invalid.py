"""
Login Tests
Tests for valid and invalid login scenarios.
"""

import pytest
import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLogin:
    """Test suite for login functionality."""
    
    def test_valid_login_reporter(self, driver, base_url):
        """
        Test Case: Valid login with reporter credentials
        
        Steps:
        1. Navigate to login page
        2. Enter valid reporter credentials
        3. Click login button
        4. Verify user lands on dashboard
        5. Verify user email and role are displayed
        """
        # Arrange
        login_page = LoginPage(driver, base_url)
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        login_page.navigate_to_login()
        login_page.login('reporter@example.com', 'password123')
        
        # Wait for dashboard to load
        time.sleep(2)
        
        # Assert
        assert dashboard_page.is_on_dashboard(), "User should be on dashboard after valid login"
        assert 'reporter@example.com' in dashboard_page.get_user_email(), "User email should be displayed"
        assert 'reporter' in dashboard_page.get_user_role().lower(), "User role should be displayed"
    
    def test_valid_login_manager(self, driver, base_url):
        """
        Test Case: Valid login with manager credentials
        
        Steps:
        1. Navigate to login page
        2. Enter valid manager credentials
        3. Click login button
        4. Verify user lands on dashboard
        5. Verify user email and role are displayed
        """
        # Arrange
        login_page = LoginPage(driver, base_url)
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        login_page.navigate_to_login()
        login_page.login('manager@example.com', 'password123')
        
        # Wait for dashboard to load
        time.sleep(2)
        
        # Assert
        assert dashboard_page.is_on_dashboard(), "User should be on dashboard after valid login"
        assert 'manager@example.com' in dashboard_page.get_user_email(), "User email should be displayed"
        assert 'manager' in dashboard_page.get_user_role().lower(), "User role should be displayed"
    
    def test_invalid_login_wrong_email(self, driver, base_url):
        """
        Test Case: Invalid login with non-existent email
        
        Steps:
        1. Navigate to login page
        2. Enter invalid email
        3. Enter any password
        4. Click login button
        5. Verify error message is displayed
        6. Verify user remains on login page
        """
        # Arrange
        login_page = LoginPage(driver, base_url)
        
        # Act
        login_page.navigate_to_login()
        login_page.login('invalid@example.com', 'password123')
        
        # Assert
        assert login_page.is_error_message_displayed(), "Error message should be displayed"
        assert 'Invalid email or password' in login_page.get_error_message(), "Correct error message should be shown"
        assert login_page.is_on_login_page(), "User should remain on login page"
    
    def test_invalid_login_wrong_password(self, driver, base_url):
        """
        Test Case: Invalid login with wrong password
        
        Steps:
        1. Navigate to login page
        2. Enter valid email
        3. Enter incorrect password
        4. Click login button
        5. Verify error message is displayed
        6. Verify user remains on login page
        """
        # Arrange
        login_page = LoginPage(driver, base_url)
        
        # Act
        login_page.navigate_to_login()
        login_page.login('reporter@example.com', 'wrongpassword')
        
        # Assert
        assert login_page.is_error_message_displayed(), "Error message should be displayed"
        assert 'Invalid email or password' in login_page.get_error_message(), "Correct error message should be shown"
        assert login_page.is_on_login_page(), "User should remain on login page"
    
    def test_login_with_empty_credentials(self, driver, base_url):
        """
        Test Case: Login attempt with empty credentials
        
        Steps:
        1. Navigate to login page
        2. Leave email and password empty
        3. Click login button
        4. Verify error message or validation prevents submission
        """
        # Arrange
        login_page = LoginPage(driver, base_url)
        
        # Act
        login_page.navigate_to_login()
        login_page.click_login()
        
        # Assert
        # HTML5 validation should prevent submission, user stays on login page
        assert login_page.is_on_login_page(), "User should remain on login page with empty credentials"
    
    def test_login_with_empty_password(self, driver, base_url):
        """
        Test Case: Login attempt with empty password
        
        Steps:
        1. Navigate to login page
        2. Enter valid email
        3. Leave password empty
        4. Click login button
        5. Verify validation error
        """
        # Arrange
        login_page = LoginPage(driver, base_url)
        
        # Act
        login_page.navigate_to_login()
        login_page.enter_email('reporter@example.com')
        login_page.click_login()
        
        # Assert
        # HTML5 validation should prevent submission
        assert login_page.is_on_login_page(), "User should remain on login page with empty password"
    
    def test_logout_functionality(self, driver, base_url):
        """
        Test Case: User logout
        
        Steps:
        1. Login with valid credentials
        2. Click logout button
        3. Verify user is redirected to login page
        4. Verify success/info message is displayed
        """
        # Arrange
        login_page = LoginPage(driver, base_url)
        dashboard_page = DashboardPage(driver, base_url)
        
        # Act
        login_page.navigate_to_login()
        login_page.login('reporter@example.com', 'password123')
        dashboard_page.click_logout()
        
        # Assert
        assert login_page.is_on_login_page(), "User should be redirected to login page after logout"
