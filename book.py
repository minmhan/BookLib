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
from category import Category

client = MongoClient('mongodb://localhost:27017/')
db = client.ebooks
fs = gridfs.GridFS(db)
validfiles = ['.pdf','.docx','.doc','.txt','.chm','.awz3']
cat = Category()
    
def insertbook(location):
    for path, subdirs, files in os.walk(location):
        for name in files:
            ext = os.path.splitext(name)[1]
            if not ext.lower() in validfiles:
                continue
            file = open(os.path.join(path,name), 'rb')
            
            if fs.exists({'filename':name}):
                continue
                
            filemetadata = get_file_metadata(os.path.join(path,name))

            booktitle = ''
            if filemetadata is not None and filemetadata['title'] is not None and filemetadata['title'] is not '':
                booktitle = filemetadata['title']
            else:
                booktitle = name.split('.')[0].replace('_',' ')
            
                
            # TODO: currently folder name is set to category
            categoryname = path.split('/')[-1]
            if not(cat.isexist(categoryname)):
                categoryname = None
            
            meta = { 
                    'title': booktitle, 
                    'desc' : '',
                    'images':[],
                    'edition':'',
                    'category':categoryname,
                    'language':'English',
                    'tags':[],
                    'isbn10':'',
                    'isbn13':'',
                    'length':None,
                    'publisher':'',
                    'author': [],
                    'amazonrank': [] 
                    }
            
            gridin = fs.new_file(filename=name,
                        contentType= get_content_type(name),
                        content = None,
                        fmd = filemetadata,
                        bmd = meta)
            gridin.write(file.read())
            gridin.close()
            print(name)


def getbooktitle():
    pass
  
    
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
    metadata = {'title':'', 'author':'','creator':'','producer':'','subject':''}
    content_type = get_content_type(file)
    if content_type == 'application/pdf':
        metaInfo = pdfutil.read_metadata(file)
        if metaInfo is not None:
            metadata['title'] = metaInfo.title
            metadata['author'] = metaInfo.author
            metadata['creator'] = metaInfo.creator
            metadata['producer'] = metaInfo.producer
            metadata['subject'] = metaInfo.subject
        return metadata
    else:
        return None
    
    
"""
TODO: Implement for others
"""
def get_file_content(file):
    content_type = get_content_type(file)
    if content_type == 'application/pdf':
        return pdfutil.read_content(file)
    else:
        return ''


def download(filename):
    location = '/media/minmhan/New Volume/EBook/Math/Misc/tmp/'
    file = fs.find_one({'filename':filename})
    f = open('/media/minmhan/New Volume/EBook/' + filename, 'wb')
    f.write(file.read())

    
    
    
    


location = '/media/minmhan/New Volume/EBook/Computer/.NET'
insertbook(location)       
#download('21 Recipes for Mining Twitter.pdf')
