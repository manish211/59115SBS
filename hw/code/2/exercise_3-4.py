# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:42:28 2015

@author: manish
"""

#def print_spam():
#    print 'spam'
#    

def print_spam(param):
    print param
   
#   
#def do_twice(f):
#    f()
#    f()
    
    
def do_twice(functionName,value):
    functionName(value)
    functionName(value)
    

    
#do_twice(print_spam)

print "================"

do_twice(print_spam,"spam")