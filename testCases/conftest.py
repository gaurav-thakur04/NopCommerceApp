from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser =='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser..........")
    elif browser == 'microsoft-edge':
        driver = webdriver.Edge()
        print("Launchind Mircosoft Edge........")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):                 #This will get the value from Command line interface
    parser.addoption("--browser")  

@pytest.fixture()
def browser(request):           #This will return the Browset value to setup method
    return request.config.getoption("--browser")


########### Pytest HTML report #######

# Hook for adding environment info to HTML Report
def pytest_configure(config):
    #config._metadata['Project Name'] = 'nop Commerce'
    #config._metadata['Module Name'] = 'Customers'
    #config._metadata['Tester'] = 'Gaurav'

    config._metadata = {
        "Tester":"Gaurav",
        "Project Name":"nop Commerce",
        "Module Name":"Customers"
        }

# Hook for delete/Modify Environment info to HTML report 

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
