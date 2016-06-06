# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:54:13 2016

@author: minmhan
"""
import datetime
from pymongo import MongoClient
import gridfs
import os
import mimetypes
import logging
import pdfutil

client = MongoClient('mongodb://localhost:27017/')
db = client.booklib
fs = gridfs.GridFS(db)
#fsb = gridfs.GridFSBucket(db)

def insertbook(location, category):
    #file_id = fs.put('hello world'.encode('utf-8'), test_metadata='testing', other_metadata='other')
    for path, subdirs, files in os.walk(location):
        for name in files:
            #print(os.path.join(path, name))
            file = open(os.path.join(path,name), 'rb')
            
            if fs.exists({'filename':name}):
                continue
                
            meta = { 'book_title': name, 
                    'book_desc' : '', 
                    'edition':'',
                    'category':category,
                    'language':'English',
                    'tags':['programming','ruby'],
                    'isbn_10':'',
                    'isbn_13':'',
                    'paperback':'',
                    'publisher':'',
                    'author': [],
                    'amazon_rank': [] }
            
            gridin = fs.new_file(filename=name,
                        content_type= get_content_type(name),
                        file_content = '',
                        file_metadata = get_file_metadata(os.path.join(path,name)),
                        book_metadata = meta)
            gridin.write(file.read())
            gridin.close()

  
    
def insert_category(category, ancestors, parent):
    for c in category:
        if(db.categories.exists({_id:c})):
            continue
        db.categories.insert({_id:c, ancestors: ancestors, parent:parent})

                        
"""
Guess content type by file extension.
"""
def get_content_type(name):
    return mimetypes.guess_type(name)[0]
    
"""
TODO: Implement for others
"""
def get_file_metadata(file):
    content_type = get_content_type(file)
    if content_type == 'application/pdf':
        return pdfutil.read_metadata(file)
    else:
        return {}
    
    
"""
TODO: Implement for others
"""
def get_file_content(file):
    content_type = get_content_type(file)
    if content_type == 'application/pdf':
        return pdfutil.read_content(file)
    else:
        return ''


def writefile():
    location = '/media/minmhan/New Volume/EBook/Math/Misc/tmp/'
    file = fs.find_one()
    #print(file.read())
    f = open('/media/minmhan/New Volume/EBook/Math/Misc/tmp/test.pdf', 'wb')
    f.write(file.read())
    
    fsb.download_to_stream_by_name('test2.pdf','/media/minmhan/New Volume/EBook/Math/Misc/tmp/')    


location = '/media/minmhan/New Volume/EBook/Computer/Ruby'
insertbook(location, 'programming,ruby')       
