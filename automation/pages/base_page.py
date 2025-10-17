"""
Base Page Object
Contains common methods used across all page objects.
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class BasePage:
    """Base class for all page objects."""
    
    def __init__(self, driver):
        """Initialize the base page with a WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def find_element(self, locator, timeout=15):
        """
        Find an element with explicit wait.
        
        Args:
            locator: Tuple of (By.LOCATOR_TYPE, 'locator_value')
            timeout: Maximum time to wait for element
            
        Returns:
            WebElement if found
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise NoSuchElementException(f"Element not found: {locator}")
    
    def find_elements(self, locator, timeout=10):
        """
        Find multiple elements with explicit wait.
        
        Args:
            locator: Tuple of (By.LOCATOR_TYPE, 'locator_value')
            timeout: Maximum time to wait for elements
            
        Returns:
            List of WebElements
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []
    
    def scroll_into_view(self, element):
        """Scroll element into view, centered in the viewport."""
        try:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
                element,
            )
        except Exception:
            pass

    def click(self, locator):
        """
        Click an element after waiting for it to be clickable.
        Includes scroll into view and JS-click fallback to avoid interception.
        
        Args:
            locator: Tuple of (By.LOCATOR_TYPE, 'locator_value')
        """
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locator)
        )
        # Try normal click with scroll and slight move
        self.scroll_into_view(element)
        try:
            ActionChains(self.driver).move_to_element(element).pause(0.05).perform()
            element.click()
            return
        except ElementClickInterceptedException:
            pass
        except Exception:
            # Try JS click as a fallback for any click interception
            pass
        try:
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            raise e
    
    def enter_text(self, locator, text):
        """
        Clear and enter text into an input field.
        
        Args:
            locator: Tuple of (By.LOCATOR_TYPE, 'locator_value')
            text: Text to enter
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """
        Get text from an element.
        
        Args:
            locator: Tuple of (By.LOCATOR_TYPE, 'locator_value')
            
        Returns:
            Text content of the element
        """
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator, timeout=10):
        """
        Check if an element is visible on the page.
        
        Args:
            locator: Tuple of (By.LOCATOR_TYPE, 'locator_value')
            timeout: Maximum time to wait
            
        Returns:
            True if visible, False otherwise
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def select_dropdown_by_value(self, locator, value):
        """
        Select an option from a dropdown by its value.
        
        Args:
            locator: Tuple of (By.LOCATOR_TYPE, 'locator_value')
            value: Value to select
        """
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)
    
    def select_dropdown_by_text(self, locator, text):
        """
        Select an option from a dropdown by visible text.
        
        Args:
            locator: Tuple of (By.LOCATOR_TYPE, 'locator_value')
            text: Visible text to select
        """
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)
    
    def get_attribute(self, locator, attribute):
        """
        Get attribute value from an element.
        
        Args:
            locator: Tuple of (By.LOCATOR_TYPE, 'locator_value')
            attribute: Attribute name
            
        Returns:
            Attribute value
        """
        element = self.find_element(locator)
        return element.get_attribute(attribute)
    
    def wait_for_url_contains(self, url_fragment, timeout=10):
        """
        Wait for URL to contain a specific fragment.
        
        Args:
            url_fragment: String that should be in URL
            timeout: Maximum time to wait
            
        Returns:
            True if URL contains fragment, False otherwise
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(url_fragment)
            )
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """Get current page URL."""
        return self.driver.current_url
    
    def refresh_page(self):
        """Refresh the current page."""
        self.driver.refresh()
