import pytest
from selenium.webdriver.edge.options import Options
from selenium import webdriver

nexus_URL = 'https://nexus-dev.ultimagen.com/'
nexus_login_URL = 'https://uma-test.app.ultimagen.com/signin/?destination=nexus'

# Input: None
# Output: Selenium webdriver
# This function assigns the webdriver to an MS Edge browser instance
def connect() -> webdriver:
    options = Options()
    options.add_argument('--guest')  # Removes the manage preferences popup in Edge
    driver = webdriver.Edge(options=options)
    driver.get(nexus_URL)
    driver.fullscreen_window()
    return driver

# Input: None
# Output: None
# This function connects the driver on test setup, gives itself to the testcase, and closes the driver on test cleanup
@pytest.fixture(scope="function")
def driver():
    driver = connect()
    yield driver
    driver.quit()


# Example test case
def test_launch_driver(driver):
    current_url = driver.current_url
    assert nexus_login_URL == current_url
    print('If it gets here, the test passed')
    assert 'Wrong URL' == current_url
    print('If it gets here, the test passed again')


# Launching point of test suite
if __name__ == '__main__':
    test_arguments = '-rA'  # -rA is an example of a test argument. 'r' displays a test result summary. 'A' shows the summary for 'all' result types (pass, fail, skipped, etc)
    test_case_files = 'main.py'  # main.py is the location of the test case above
    test_output = '--html=TestFile.html'  # name of results will be in local file named TestFile.html
    test_output_config = '--self-contained-html'  # CSS file built into the html file
    pytest.main([test_arguments, test_case_files, test_output, test_output_config])