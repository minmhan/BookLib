# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:54:13 2016

PDF Utility by using PyPDF2 Library
"""
from PyPDF2 import PdfFileReader

def read_content(fname):
    s = ""
    pdf = PdfFileReader(open(fname, 'rb'))
    for page in pdf.pages:
        s += page.extractText()
    s = " ".join(s.replace("\xa0", " ").strip().split())
    return s

def read_metadata(fname):
    pdf = PdfFileReader(open(fname, 'rb'))
    return pdf.getDocumentInfo()
