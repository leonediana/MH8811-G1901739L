#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:04:15 2019

@author: leone
"""


def tictacdraw(board):
    n=len(board)
    for i in range(n):
        ss=''
        for b in range(n):
            if board[i][b]==0:
                ss+='o'
            elif board[i][b]==1:
                ss+='x'
            elif board[i][b]==2:
                ss+=' '
                if i>0:
                    print((4*n-1)*'-')
        str=' | '
        ss=str.join(ss)
        print(' '+ss)


tictacdraw([ [ 0, 1, 2 ], [ 2, 0, 0 ], [ 1, 1, 2]])







        