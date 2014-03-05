#See http://selenium-python.readthedocs.org/en/latest/getting-started.html
# See http://sqa.stackexchange.com/questions/1355/what-is-the-correct-way-to-select-an-option-using-seleniums-python-webdriver
# See http://selenium.googlecode.com/svn/trunk/docs/api/py/webdriver_support/selenium.webdriver.support.select.html
# WATIR or Selenium to handle pages with Javascript
# TODO: Use results to load wordpress site.
# Use Beautifulsoup to parse html
# TODO: Create a separate file for google data
#Note: Pycharm community does not support webdevelopment.  Professional edition does.

URL_NAME = "http://change_me"

import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


# Write results to file
f = open('change_me.txt', 'w')


# create an instance of Firefox WebDriver
driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds

# Navigate
driver.get(URL_NAME)

assert "CHANGE_ME" in driver.title

#Get element by name 'zipCode' then assign all options with value to a tuple for iteration
select = Select(driver.find_element_by_name('zipCode'))

#http://stackoverflow.com/questions/18515692/listing-select-option-values-with-selenium-and-python
#http://docs.seleniumhq.org/exceptions/stale_element_reference.jsp
all_options = select.options
zips = [opt.get_attribute("value") for opt in all_options]
data = dict.fromkeys(zips, {})
for zc in zips:
    print ("Value is: %s" % zc)
    select = Select(driver.find_element_by_name('zipCode'))

    select.select_by_value(zc)
    select.first_selected_option.click()

    submit_button = driver.find_element_by_name("Submit")
    webdriver.ActionChains(driver).move_to_element(submit_button).click(submit_button).perform()

