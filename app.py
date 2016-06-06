# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 19:15:26 2016

@author: minmhan
"""
import sys, getopt
import logging

def main(argv):
    operation = ''
    try:
        opts, args = getopt.getopt(argv, "ho")
    except getopt.GetoptError:
        print('app.py')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('app.py -o import -')
            sys.exit()
        elif opt == '-o':
            operation = arg
    
    
    if operation == 'import':
        pass
    elif operation == 'export':
        pass
    elif operation == 'update':
        pass
        
    print('operation:', operation)



if __name__ == "__main__" :
    main(sys.argv[1:])        