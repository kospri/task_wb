#!/usr/bin/python

import os.path
from ConfigParser import SafeConfigParser
from tf.elem_locator import ElementLocator, ElementType

class ConfigReader(object):
    '''
    Read configuration file. 
    Set section name according to ClassName, that is equal section in configuration file
    '''    
    def __init__(self, page_name):                
        self._cfg = SafeConfigParser()
        self._filepath = search_from_curdir("mapping.cfg")
        if (os.path.isfile(self._filepath)):
            self._cfg.read(self._filepath)
            self._PageName = page_name
        else:
            assert 'Configuration file does not exist!' == self._filepath
    
    def get_locator(self, element_name):
        ''' 
        Get locator for the element by its name on current page
        
        :Args:
            element_name - String, name of the element in the mapping file.
            
        :Usage:
            config.get_locator('search_link')
        '''
        value = self._cfg.get(self._PageName, element_name)
        i = value.find(',')
        if (i != -1):
            sub_type = value[:i]
            if (sub_type == ElementType.XPATH):
                value = ElementLocator(ElementType.XPATH, value[i+1:])
            elif (sub_type == ElementType.CSS):
                value = ElementLocator(ElementType.CSS, value[i+1:])
            elif (sub_type == ElementType.ID):
                value = ElementLocator(ElementType.ID, value[i+1:])
            elif (sub_type == ElementType.NAME):
                value = ElementLocator(ElementType.NAME, value[i+1:])
        return value
    
    def get_page_locator(self, page, element_name):
        ''' 
        Return locator of specifed element on specified page
        
        :Args:
            page - page name
            element_name - element name
        
        :Usage:
            config.get_page_locator('Site', 'url') 
        '''
        return self._cfg.get(page, element_name)


def search_from_curdir(file_name):
    '''
    'Private' method 
    Search file from current dir and then upper in parent folders 
    
    Return full path to file or None (if not found)
    
    :Args:
        file_name - name of the file with configuration parameters
        
    :Usage:
        cf_reader.search_from_curdir("config.ini")
    '''         
    if (os.path.exists(file_name)):
        return os.path.abspath(file_name)
       
    cur_dir = os.getcwd()
    res = os.path.join(cur_dir, file_name)
    
    if (os.path.exists(res)):
        return res
    
    new_dir = os.path.dirname(cur_dir)
        
    while (new_dir != cur_dir):
        cur_dir = new_dir
        res = os.path.join(cur_dir, file_name)
        
        if os.path.exists(res):
            return res                
        new_dir = os.path.dirname(cur_dir)
    return None
