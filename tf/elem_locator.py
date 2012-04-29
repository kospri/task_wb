#!/usr/bin/python

from selenium.webdriver.common.by import By

class ElementType(object):
    ID    = 'id'
    NAME  = 'name'
    CSS   = 'css'
    XPATH = 'xpath'

class ElementLocator(object):
    ''' Element locator implementation '''

    def __init__(self, by_type, locator):
        self._by_type = by_type
        self._locator = locator
        
    def get_by_type(self):
        return self._by_type
    
    def get_locator_value(self):
        return self._locator
    
    def set_by_type(self, by_type):
        self._by_type
        
    def set_locator_value(self, locator):
        self._locator = locator
        
    def get_selenium_by(self):
        if (self._by_type == ElementType.ID):
            return By.ID
        elif (self._by_type == ElementType.NAME):
            return By.NAME
        elif (self._by_type == ElementType.CSS):
            return By.CSS_SELECTOR
        elif (self._by_type == ElementType.XPATH):
            return By.XPATH
        return None
        