# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:14:29 2024

@author: ADMINIS
"""

N = int(input("Nhập vào số N nguyên dương: "))
while N <= 0:
    N = int(input("Nhập lại số N nguyên dương: "))
x = 0
while N>0:
    x = x +N%10
    N = N//10
print("Tổng các chữ số của N là:", x)