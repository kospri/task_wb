#!/usr/bin/python

class Page(object):
    ''' 
    Common Page object implementation 
    '''

    def __init__(self, browser, page_url, load = False):
        self._browser = browser
        self._page_url = page_url
        
        if (load):
            self._browser.get(self._page_url)
            
    def title(self):
        ''' 
        Returns the title of the page
        '''
        return self._browser.title()
        
        
    def verify_page(self):
        pass
        