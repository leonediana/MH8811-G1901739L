#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:50:25 2019

@author: leone
"""

def func1():
    print('hello,world')

#---------------------------------

def func2():
    name=input('what is your name?')
    print('hello,',name)
    
#---------------------------------

def func3():
    c=input('the value of celsius')
    C=float(c)
    F=C*1.8+3.2
    print(F)

#---------------------------------


while True: 
    choice= input('do you want to run function 1, function 2 or function 3?')
    
    if choice=='function 1':
        func1()
        answer=input('do you wanna continue? YES or NO')
        if answer == 'YES':
            continue 
        else:
            break            
    if choice=='function 2':
        func2()
        answer=input('do you wanna continue? YES or NO')
        if answer == 'YES':
            continue 
        else:
            break
    if choice=='function 3':
        func3() 
        answer=input('do you wanna continue? YES or NO')
        if answer == 'YES':
            continue 
        else:
            break
    else:
        break
print('done')