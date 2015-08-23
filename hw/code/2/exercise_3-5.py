# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:55:26 2015

@author: manish
"""

def draw_grid(rows,cols):
    for i in range(rows):
        print "+ - - - -"*cols+"+"
        print ("|" + "  "*4)*cols+"|"
        print ("|" + "  "*4)*cols+"|"
        print ("|" + "  "*4)*cols+"|"
        print ("|" + "  "*4)*cols+"|"
        
    print "+ - - - -"*cols+"+"     
 
    

draw_grid(2,2)

print  
print "GRID 4X4 BELOW"

draw_grid(4,4)