# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 21:49:28 2016

@author: minmhan
"""

import urllib
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class crawler:
    def __init__(self):
        pass
    
    def __del__self(self):
        pass
    
    
    # Auxilliary function for getting an entry id and adding it if it's not present
    def getentryid(self,table,field,value,createnew=True):
        return None
    
    # Index an individual page
    def addtoindex(self,url,soup):
        print('Indexing:', url)
    
    # Extract the text from an HTML page (no tags)
    def gettextonly(self,soup):
        return None
    
    # Separate the words by any non-whitespace character
    def separatewords(self,text):
        return None
    
    # Return true if this url is already indexed
    def isindexed(self,url):
        return False
    
    # Add a link between two pages
    def addlinkref(self,urlFrom,urlTo,linkText):
        pass
    
    def crawl(self, pages, depth=2):
        pass
    
    # Create the database tables
    def createindextables(self):
        pass

