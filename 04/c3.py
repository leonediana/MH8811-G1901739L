#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:43:51 2019

@author: leone
"""

def getfilelines(file):
    fhandle=open(file)
    lines=[]
    for line in fhandle:
        line=line.rstrip()
        if line:
            line=float(line)
            lines.append(line)
    return lines 

#basic descriptive statistics
data=getfilelines('data.csv')
print(data)
print('the max number is:',my_max(data))
print('the min number is:',my_min(data))
print('the average number is:',my_average(data))
print('the median number is:',my_median(data))
print('the range of the list is:',my_range(data))