#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:48:26 2019

@author: leone
"""
#define variance function 
def my_variance(data):
    n=sum1=sum2=0
    for x in data:
        n+=1
        sum1+=x
    mean=sum1/n
    
    for x in data:
        sum2+=(x-mean)*(x-mean)
    variance=sum2/(n-1)
    return variance 

#read data
    
data=getfilelines('data.csv')

##calulate and output result

my_variance(data)
print('the sample variance is:',my_variance(data))