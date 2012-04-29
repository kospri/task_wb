#!/usr/bin/python

from tf.configreader import ConfigReader
from tf.page import Page
from tf.homepage import HomePage
from tf.rectranspage import RecentTransPage
from tf.searchnewspage import SearchNewsPage
from tf.element import Element

class MainPage(Page):
    '''
    MainPage
    '''
    
    def __init__(self, browser, load=True):
        self._config = ConfigReader(self.__class__.__name__)
        url = self._config.get_page_locator('Url', 'url') + \
                self._config.get_locator('url')
        Page.__init__(self, browser, url, load)
    
    def logout(self):
        elem = Element(self._browser, self._config.get_locator('logout_link'))
        elem.click()
        
        page = HomePage(self._browser, False)
        assert page.is_logged_in() == False
        return page
    
    def open_recent_transactions_page(self):
        elem = Element(self._browser, self._config.get_locator('recent_trans_link'))
        elem.click()
        
        page = RecentTransPage(self._browser, False)
        return page
    
    def open_search_news_page(self):
        elem = Element(self._browser, self._config.get_locator('search_news_link'))
        elem.click()
        
        page = SearchNewsPage(self._browser, False)
        return page       