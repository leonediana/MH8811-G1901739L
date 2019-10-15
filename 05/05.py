#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:43:18 2019

@author: leone
"""

import json

#define open_file function 
def op_f(s):
    hh=open(s)
    data=json.load(hh)
    hh.close()
    return data
    

#define serialize function 
def serialize(lst):
    s=json.dumps(lst)
    return s

#define dictionary comparison function 
def dict_com(d1,d2):
    if d1 and d2: #not empty
       for k in set(d1) or set(d2): # iteration of key in dict 1 and dict 2
        if k in d1 and d2:
            if d1[k]==d2[k]:
                return True
        else:
            return False 
    elif d1==d2:
        return True
    else:
        return False
        
#define list comparison function 
def lst_com(d1,d2):
    if d1==d2:
        return True
    else:
        return False
        
            

#define comparison function 
def my_comparison(d1,d2):
    if type(d1)==type(d2):
        if type(d1)==type([]):
            print(lst_com(d1,d2))
        if type(d1)==type({}):
            print(dict_com(d1,d2))
    else:
        print('false')


            
#input file
file_name=input('H1-1,H1-2.H1-3,H1-4,H1-5?')

#load data structure from json
data1=op_f(file_name)
print(data1)
print('road done',type(data1))
    
#convert data structure to string

s=serialize(data1)
print(type(s)) 
##write string to file
file_name2=input('what is the file name?')
with open(file_name2,'w') as f:
    json.dump(s,f)
    f.close()
    print('write done')

##read string back from file
with open(file_name2, 'r') as f:
       data2=json.load(f)
       f.close()
print('road done')
print(data2)
##pass to deserialize function 
data2=json.loads(data2)
#comparison

my_comparison(data1,data2)

 

    

