__author__ = 'Christie'
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.google.com')
assert 'Google' in browser.title

#browser.get('http://www.yahoo.com')
#assert 'Yahoo' in browser.title
#elem = browser.find_element_by_name('p')  # Find the Yahoo search box
elem = browser.find_element_by_name('q')  # Find the Google search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
