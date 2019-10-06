#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:39:30 2019

@author: leone
"""
lst=[9,41,12,3,74,15]

def my_min(lst):
    minimum_number=None
    for the_num in lst:
        if minimum_number is None:
            minimum_number=the_num
        else:
            if the_num < minimum_number:
                minimum_number=the_num
    return minimum_number


#---------------------------------------------
def my_max(lst):
    max_number=None
    for the_num in lst:
        if max_number is None:
            max_number=the_num
        else:
            if the_num > max_number:
                max_number=the_num
    return max_number

#---------------------------------------------
def my_average(lst):
    sum=0
    for i in lst:
        sum=sum+i 
    ave=sum/len(lst)
    return ave

#---------------------------------------------
def my_median(lst):
    lst=sorted(lst)
    r=int(len(lst)/2)   
    if len(lst)%2!=0:
        median=lst[r]
    if len(lst)%2==0:
        median=(lst[r]+lst[r-1])/2
    return median
#---------------------------------------------

def my_range(lst):
    a=my_max(lst)
    b=my_min(lst)
    range_=a-b
    return(range_)

print(lst)
print('the max number is:',my_max(lst))
print('the min number is:',my_min(lst))
print('the average number is:',my_average(lst))
print('the median number is:',my_median(lst))
print('the range of the list is:',my_range(lst))

        


                
        
