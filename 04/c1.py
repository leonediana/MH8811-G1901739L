#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:39:30 2019

@author: leone
"""

minimum_number=None
a=[9,41,12,3,74,15]
for the_number in [9,41,12,3,74,15]:
    if minimum_number is None:
        minimum_number=the_number
    else:
        if the_number < minimum_number:
            minimum_number=the_number
print(a)
print(minimum_number)

        


                
        
