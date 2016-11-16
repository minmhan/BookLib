# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:32:27 2016

@author: minmhan
"""

from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import datetime
import MySQLdb
from contextlib import closing

#TODO: exception handling
url = 'http://www.allitebooks.com'
MAX_FILE_SIZE = 100 # max allow 100MB download
class crawler:
    def __init__(self, dbname):
        self.con=MySQLdb.connect("localhost", "minmhan","P@ssw0rd", "allitebooks", charset='utf8')
        
    def __del__self(self):
        self.con.close()
        
    def dbcommit(self):
        self.con.commit()
    
    # Index an individual page
    def addtoindex(self,url,soup):
        if self.isindexed(url):
            return
        else:
            with closing(self.con.cursor()) as cur:
                cur.execute("insert into urllist (url,created_at) values ('%s', '%s')" % (url,datetime.datetime.now()))
                cur.close()
        
        
    def updatestatus(self, url):
        with closing(self.con.cursor()) as cur:
            cur.execute("update urllist set status='success' where url='%s'" % url)
    

    # Extract the text from an HTML page (no tags)
    def gettextonly(self,soup):
        v=soup.string
        if v==None:
            c=soup.contents
            resulttext=''
            for t in c:
                subtext=self.gettextonly(t)
                resulttext+=subtext+'\n'
            return resulttext
        else:
            return v.strip()
            
    
    # Separate the words by any non-whitespace character
    def separatewords(self,text):
        splitter=re.compile('\\W*')
        return [s.lower() for s in splitter.split(text) if s!='']
    
    # Return true if this url is already indexed
    def isindexed(self,url):
        with closing(self.con.cursor()) as cur:
            u=cur.execute("select id from urllist where url='%s'" % url)
            if u!=0:
                return True
            else:
                return False
    
    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages=set()
            for page in pages:
                print('crawling %s' % page)
                try:
                    c=request.urlopen(page)
                except:
                    print('could not open %s' % page)
                    continue
                
                soup = BeautifulSoup(c.read(), 'html.parser')
                
                self.addtoindex(page,soup)
                links=soup('a')
                for link in links:
                    if('href' in dict(link.attrs)):
                        url= urljoin(page,link['href'])
                        if url.find("'")!=-1: continue
                        url=url.split('#')[0] #remove location portion
                        #url=url.replace(u"\u2018","'").replace(u"\u2019","'")
                        if url[0:4]=='http' and self.is_ascii(url) and not self.isindexed(url):
                            newpages.add(url)
            
                # Download if single profile page
                if soup.find('body', class_='single-post') != None:
                    self.download(soup, page)
                    #self.updatestatus(page)
                    
                self.dbcommit()    
            pages = newpages

            
    def is_ascii(self, s):
        return all(ord(c) < 128 for c in s)
    
        
    def download(self, soup, page):
        book = self.extract_content(soup)          
        if book.filesize > 100: #100MB, TODO: update fail status.
            return
            
        # download pdf file
        # TODO: other format
        link = soup.find(href=re.compile('.pdf$', re.IGNORECASE))
        url = urljoin(page, link['href'])
        
        book.url = url
        book.file, book.filename = self.download_file(url)

        # download image file        
        imgLink = soup.find('img', class_='attachment-post-thumbnail')
        url = urljoin(page,imgLink['src'])
        book.image, book.imagefilename = self.download_file(url)
        
        self.addbook(book)
        

    def extract_content(self, soup):
        book = Book()        
        book.title = soup.find('h1', class_='single-title').get_text()
        book.desc = soup.find('div', class_='entry-content').get_text()
        book_detail = soup.find('div', class_='book-detail')
        for c in book_detail.select("dt"):
            if c.string == 'Isbn:':
                book.isbn = c.next_sibling.get_text()
            if c.string == 'Year:':
                try:
                    book.year = int(c.next_sibling.get_text())
                except:
                    print('could not parse year')
            if c.string == 'Pages:':
                try:
                    book.pages = int(c.next_sibling.get_text())
                except:
                    print('could not parse pages')
            if c.string == 'File size:':
                try:
                    filesize = c.next_sibling.get_text()
                    filesize = filesize.replace('MB','')
                    book.filesize = float(filesize)
                except:
                    print('could not parse file size')
            if c.string == 'File format:':
                book.fileformat = c.next_sibling.get_text()
            if c.string == 'Category:':
                book.category = c.next_sibling.get_text()
            if c.string == 'Author:':
                book.author = c.next_sibling.get_text()
            
        return book
        
                         
    def download_file(self, url):
        print('downloading %s' % url.replace(' ', '%20'))
        try:
            req = request.urlopen(url.replace(' ','%20'))
        except:
            print('could not open %s' % url.replace(' ', '%20'))
            return
        
        filename = url.split('/')[-1]
        data = req.read()
        req.close()
        return (data,filename)
        
        
    def addbook(self, book):  
        with closing(self.con.cursor()) as cur:
            # insert file
            query = "insert into file(file,filename) values (%s,%s)"
            args = (book.file, book.filename)
            cur.execute(query, args)
            fileid = cur.lastrowid
            # insert image file
            query = "insert into image(image,filename) values (%s,%s)"
            args = (book.image, book.imagefilename)
            cur.execute(query, args)
            imageid=cur.lastrowid
            # insert book
            query = """insert into book(file_id, image_id, title,author,isbn,year,pages,filesize,
                            fileformat,category,description,url,created_at)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            args = (fileid, imageid, book.title,book.author,book.isbn,book.year,
                        book.pages,book.filesize,book.fileformat,
                        book.category,book.desc,book.url,datetime.datetime.now())
            cur.execute(query, args)


    # download file from database
    def getbook(self, title):
        with closing(self.con.cursor()) as cur:
            cur.execute("select file_id from book where title='%s'" % (title))
            if cur.lastrowid != 0:
                self.getfile('book',cur.lastrowid)
            else:
                print("%s not found." % title)

            
    # download image from database
    def getimage(self, title):
        with closing(self.con.cursor()) as cur:
            cur.execute("select image_id from image where title='%s'" % (title))
            if cur.lastrowid != 0:
                self.getfile('image', cur.lastrowid)
            else:
                print("%s not found." % title)
    
    
    def getfile(self,table, id):
        with closing(self.con.cursor()) as cur:
            cur.execute("select %s,filename from image where id=%d" % (table,id))
            f = cur.fetchone()
            with open(f[1], 'wb') as file:
                file.write(f[0])
            
        
    # Create the database tables
    def createindextables(self):
        self.con.cursor().execute("""create table if not exists book(id INTEGER AUTO_INCREMENT,
                file_id INTEGER,image_id INTEGER,title VARCHAR(255), author VARCHAR(255),
                isbn VARCHAR(20),year INTEGER,pages INTEGER, filesize DECIMAL(10,2),
                fileformat VARCHAR(10),category VARCHAR(255),description TEXT,url VARCHAR(255),
                created_at DATETIME,primary key(id))""")
        self.con.cursor().execute("""create table if not exists file(id INTEGER AUTO_INCREMENT, 
                file LONGBLOB, filename VARCHAR(100), primary key(id))""")
        self.con.cursor().execute("""create table if not exists image(id INTEGER AUTO_INCREMENT, 
                image MEDIUMBLOB, filename VARCHAR(100), primary key(id))""")
        self.con.cursor().execute("""create table if not exists urllist(id INTEGER AUTO_INCREMENT, 
                url VARCHAR(255), status VARCHAR(10), created_at DATETIME, primary key(id))""")
        #self.con.execute('create index urlidx on urllist(url)')

        
class Book:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
    

pagelist=['http://www.allitebooks.com']
c = crawler('allitebooks.db')
#c.createindextables()
#c.crawl(pagelist)
#print([row for row in c.con.execute('select rowid from wordlocation where wordid=1')])

#c.download_file('http://file.allitebooks.com/20151012/Parallelism%20in%20Matrix%20Computations.pdf')
#c.crawl(['http://www.allitebooks.com/parallelism-in-matrix-computations/'],2)
c.crawl(pagelist,2)


















