# AutomatedTestSuiteNEX

## Purpose
The purpose of this project is to automate the web UI and the API of the Nexus web application

## Installation Instructions
 ### Install MS Edge Web Driver
  1. Navigate to https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH
  2. Install the latest **Stable Channel** for a x64 environment
  3. Set Environment PATH variable to msedgedriver.exe directory (should create a folder in C driver named WebDrivers)
 ### Install packages
  1. Navigate to virtual environment
  2. Enter in venv terminal: pip install -r .\Misc\requirements.txt
   (can also install through cmd if preferred)
   
## Package Details
| **Package**     | **Purpose**      | **Documentation** |
| ------------- | ------------- | ------------- |
| assertpy   | This package is responsible for all assertions in this test library, to ensure that the required steps and results are executed as expected | https://github.com/assertpy/assertpy |
| Pytest     | The testing framework responsible to deciding which tests are executed, the testing format, and testing configurations. | https://docs.pytest.org/en/8.2.x/ |
| Pytest-html   | Output of the pytest tests; upon completion of a test run, an html file will be created with results. | https://pytest-html.readthedocs.io/en/latest/user_guide.html |
| requests     | Library which supports GET and POST requests in python. | https://pypi.org/project/requests/ |
| selenium   | Library responsible for connecting to the Edge webdriver and interacting with the webpage. | https://www.selenium.dev/documentation/overview/ |
