#!/usr/bin/python

from tf.element import Element

class TextBox(Element):
    '''
    TextBox
    '''


    def __init__(self, browser, locator):
        Element.__init__(self, browser, locator)
        
    def clear(self):
        '''
        Clear text
        '''
        self.get_web_element().clear()
        
    def set_text(self, text):
        '''
        Clear & set text
        '''
        elem = self.get_web_element()
        elem.clear()
        elem.send_keys(text)
        
    def append_text(self, text):
        '''
        Append text to the end
        '''
        elem = self.get_web_element()        
        elem.send_keys(text)
        
    def get_text(self):
        '''
        get text from the textBox
        '''
        return self.get_web_element().get_text()
    
    def get_value(self):
        '''
        get text value from TextBox
        '''
        return self.get_attribute('value')
    
    