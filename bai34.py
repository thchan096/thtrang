# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:52:54 2024

@author: ADMINIS
"""

N = int(input("Nhập số nguyên dương N: "))
while N <= 0:
    N = int(input("Nhập lại số nguyên dương N: "))
if N == 1:
    print("1 không phải là số nguyên tố")
elif N == 2:
    print("2 là số nguyên tố")
else:
    x = False
    for i in range(2, N-1):
        if N%i == 0:
           x = True
           break
    if x:
           print(f"{N} không phải là số nguyên tố")
    else:
       print(f"{N} là số nguyên tố")