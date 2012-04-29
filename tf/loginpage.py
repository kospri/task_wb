#!/usr/bin/python


from tf.configreader import ConfigReader

from tf.textbox import TextBox
from tf.element import Element

from page import Page


class LoginPage(Page):
    '''
    LoginPage
    '''

    def __init__(self, browser, load=False):
        self._config = ConfigReader(self.__class__.__name__)
        url = self._config.get_page_locator('Url', 'url') + \
                self._config.get_locator('url')
        Page.__init__(self, browser, url, load)
        
    def login(self, user, password):
        from mainpage import MainPage
        from homepage import HomePage
        
        box = TextBox(self._browser, self._config.get_locator('username'))
        box.set_text(user)
        box.set_locator(self._config.get_locator('password'))
        box.set_text(password)
        elem = Element(self._browser, self._config.get_locator('submit'))
        elem.click()
        
        page = HomePage(self._browser, False)
        if not page.is_logged_in():
            msg = "Login failed"
            box.set_locator(self._config.get_locator('err_msg'))
            if (box.exists()):
                msg = box.get_text()
            assert msg == ''
        return MainPage(self._browser, False)