#!/usr/bin/python


from tf.element import Element
from tf.configreader import ConfigReader

from tf.page import Page
from loginpage import LoginPage

from selenium.webdriver import Firefox

class HomePage(Page):
    '''
    HomePage
    '''

    def __init__(self, browser, load=True):
        self._config = ConfigReader("HomePage")
        page_url = self._config.get_page_locator('Url', 'url') + \
                    self._config.get_locator('url')
        Page.__init__(self, browser, page_url, load)
    
    def is_logged_in(self):
        elem = Element(self._browser, self._config.get_locator('login_link'))
        return not (elem.exists() and elem.is_visible())
    
    def get_login_page(self):
        if not self.is_logged_in():
            elem = Element(self._browser, self._config.get_locator('login_link'))
            elem.click()
            return LoginPage(self._browser)
        return self
   


if __name__ == '__main__':
    browser = Firefox()
    
    portal = HomePage(browser)  
    browser.stop()
