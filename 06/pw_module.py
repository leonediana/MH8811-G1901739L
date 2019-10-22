#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:13:46 2019

@author: leone
"""
import random as rd
a='zxcvbnmasdfghjklqwertyuiop'
b='ZXCVBNMASDFGHJKLQWERTYUIOP'
c='0123456789'
d='~`!@#$%^&*()-=+[]\|}{;:<>,.'
lst=[a,b,c,d]

def genpassword(n):
    pwd=''
    for a in lst:
        pwd+=rd.choice(a)
    i=4
    while i<n:
        pwd+=rd.choice(rd.choice(lst))
        i+=1
    return pwd



if __name__ == "__main__" :
    print(genpassword(12))
 
    