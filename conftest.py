import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def browser():
    pytest.driver = webdriver.Chrome('F:/cromedriver/chromedriver.exe')
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('https://www.alza.cz/')

    yield

    pytest.driver.quit()

