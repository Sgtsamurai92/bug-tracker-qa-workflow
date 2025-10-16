"""Package initialization for page objects."""

from .base_page import BasePage
from .login_page import LoginPage
from .dashboard_page import DashboardPage
from .bug_form_page import BugFormPage

__all__ = ['BasePage', 'LoginPage', 'DashboardPage', 'BugFormPage']
