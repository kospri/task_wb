#!/usr/bin/python

from tf.configreader import ConfigReader
from tf.page import Page
from tf.element import Element
from tf.textbox import TextBox

class SearchNewsPage(Page):
    '''
    Search News Articles page
    '''

    def __init__(self, browser, load=True):
        self._config = ConfigReader(self.__class__.__name__)
        page_url = self._config.get_page_locator('Url', 'url') + \
                self._config.get_locator('url') 
        Page.__init__(self, browser, page_url, load)
        
    def search_news_articles(self, search_query):
        '''
        Search news articles according to given text
        
        :Args:
            search_query - text to find.
            
        :Usage:
            page.search_news_articles('weather')
        '''
        box = TextBox(self._browser, self._config.get_locator('search_text'))
        box.set_text(search_query)
        elem = Element(self._browser, self._config.get_locator('search_btn'))
        elem.click()
        
        return self
    
    def count_search_resutls(self):
        box = TextBox(self._browser, self._config.get_locator('result_lbl'))
        if (box.get_text().find('not found') != -1):
            return 0
        return 1
        
        