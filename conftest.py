#!/usr/bin/python

from selenium.webdriver import Firefox

def pytest_funcarg__browser(request):
    '''
    Test configuration environment. Py.test pulls this in at startup.
    '''

    try:
        browser = Firefox()    
    except Exception, msg:
        raise Exception("Unable to create and start Selenium" +  
                        " object.View exception:\n\t%s" % msg)

    # Make sure we stop the browser session after each test
    request.addfinalizer(lambda: browser.close())

    return browser
