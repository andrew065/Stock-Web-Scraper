import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time

driver = webdriver.Chrome()
driver.get('https://www.macrotrends.net/stocks/charts/CVS/cvs-health/stock-price-history')

soup = BeautifulSoup(driver.page_source, 'lxml')

try:
    elements = driver.find_element(By.ID, "main_content")

    for element in elements.find_elements(By.ID, 'chart_container col-xs-12'):
        print(element.get_attribute('innerHTML'))

    print('\nbreak\n', elements.get_attribute('innerHTML'))

except selenium.common.exceptions.NoSuchCookieException:
    print("Button click unsuccessful")
    driver.close()

driver.close()
