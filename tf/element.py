#!/usr/bin/python


from selenium.common.exceptions import NoSuchElementException
from elem_locator import ElementType

#from selenium.webdriver.remote import webelement

class Element(object):
    ''' Common Element object model implementation '''
    
    def __init__(self, browser, elem_loc):
        self._browser = browser
        self._locator = elem_loc
        
    def set_locator(self, new_locator):
        '''
        Update element's locator
        :Args:
            new_locator - common locator type
        :Usage:
            element.set_locator(ElementLocator(ElementType.ID,"id1"))
        '''
        self._locator = new_locator
        
    def exists(self):
        '''
        Checks if current element exists on the page
        
        :Usage:
            element.exists()
        '''
        elem = self.get_web_element(False)
        return elem != None
    
    def is_visible(self):
        '''
        Checks if current element is visible on the page
        
        :Usage:
            element.is_visible()
        '''
        elem = self.get_web_element()
        return elem.is_displayed()
    
    def click(self):
        '''
        Click on the element
        
        :Usage:
            element.click()
        '''
        self.get_web_element().click()
        
    def get_attribute(self, attribute_name):
        '''
        Get the specified attribute value
        
        :Args:
            attribute_name - the name of the attribute
            
        :Usage:
            element.get_attribute("value")
        '''
        return self.get_web_element().get_attribute(attribute_name)
    
    def is_enabled(self):
        '''
        Checks if current element is enabled or not
        
        :Usage:
            element.is_enabled()
        '''
        return self.get_web_element().is_enabled()
    
    def find_web_element(self, elem_locator):
        ''' 
        Try to find child WebElement using custom locator type
        
        Returns WebElement object or None
        
        :Args:
            elem_locator - custom element locator type
            
        :Usage:
            element.find_web_element(ElementLocator(ElementType.ID, "id3"))
        '''
        try:
            elem_web = self.get_web_element()
            return elem_web.find_element(elem_locator.get_selenium_by(),
                                         elem_locator.get_locator_value)
        except NoSuchElementException:
                return None
        
    def get_web_element(self, with_exception=True):
        ''' 
        'Private' method
        
        Return WebElement object for this element.
        if element doen't exists - return None (if with_exception=False),
        otherwise throw NoSuchElementException
        :Usage:
            element.get_web_element()
        '''
        try:
            #return self._browser.find_element(self._locator.get_selenium_by(),
            #                                  self._locator.get_locator_value)
            elem = self.__get_webelement()
            if elem is None: raise NoSuchElementException("s")
            return elem
        except NoSuchElementException, e:
            if (with_exception == True):
                raise e
            return None
    
    def __get_webelement(self):
        if (self._locator.get_by_type() == ElementType.ID):
            return self._browser.find_element_by_id(self._locator.get_locator_value())
        if (self._locator.get_by_type() == ElementType.XPATH):
            return self._browser.find_element_by_xpath(self._locator.get_locator_value())
        if (self._locator.get_by_type() == ElementType.CSS):
            return self.\
                _browser.find_element_by_css_selector(self._locator.get_locator_value())
        if (self._locator.get_by_type() == ElementType.NAME):
            return self._browser.find_element_by_name(self._locator.get_locator_value())
        return None