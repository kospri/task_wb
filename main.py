#!/usr/bin/python

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("http://www.yahoo.com")
assert "Yahoo!" in browser.title()

elem = browser.find_element_by_name("p")
elem.send_keys("selenium_hq" + Keys.RETURN)

time.sleep(0.2)

try:
    browser.find_element_by_xpath("//a[contains(@href, 'seleniumhq.com')]")
    
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close()
#
#if __name__ == '__main__':
#    pass