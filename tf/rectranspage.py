#!/usr/bin/python

from tf.configreader import ConfigReader

from tf.page import Page

from tf.textbox import TextBox
from tf.element import Element

class RecentTransPage(Page):
    '''
    View Recent Transaction
    '''

    def __init__(self, browser, load = True):
        self._config = ConfigReader(self.__class__.__name__)
        page_url = self._config.get_page_locator('Url', 'url') + \
                self._config.get_locator('url')
        Page.__init__(self, browser, page_url, load)
        
    def search_transaction(self, after_date, before_date):
        '''
        Start searching transactions 
        in the range from [before_date] to the [after_date]
        
        :Args:
            before_date - String, before date [format: mm/dd/yyyy]
            after_date - String, after date [format: mm/dd/yyyy]
        
        :Usage:
            page.search_transaction('01/04/1920','04/04/2011')
        '''
        box = TextBox(self._browser, self._config.get_locator('after_date'))
        box.set_text(after_date)
        box.set_locator('before_date')
        box.set_text(before_date)
        elem = Element(self._browser, self._config.get_locator('submit_btn'))
        elem.click()
        
        return self
    
    def get_results_count(self):
        pass
    
    
    