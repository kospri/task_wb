#!/usr/bin/python

from tf.homepage import HomePage

def test_correct_login(browser):
    hm = HomePage(browser)
    hm.get_login_page().login('admin', 'password')
    
    

from selenium.webdriver import Firefox

b = Firefox()

test_correct_login(b)