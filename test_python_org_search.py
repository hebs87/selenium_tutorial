# ------------------------------ TEST TO SEE IF WEBDRIVER CONNECTS SUCCESSFULLY ------------------------------
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://www.google.com/');
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# driver.quit()
#
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Above example using unittest
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        """
        Set up the connection to the driver
        """
        # Specify path in parenthesis if it's not added to system path
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        """
        A test that checks that the page title has "Python" in it and then submits "pycon" in the search field.
        It then asserts that "No results found." is not in the page when the search is complete
        """
        driver = self.driver
        driver.get('http://www.python.org')
        self.assertIn("Python", driver.title)
        # Get the search field by its name attribute
        elem = driver.find_element_by_name('q')
        # Clear the element first
        elem.clear()
        # Type "pycon" in the search field and press RETURN
        elem.send_keys("pycon", Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self) -> None:
        """
        Close the webdriver connection
        """
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
