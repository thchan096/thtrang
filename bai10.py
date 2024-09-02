# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:56:38 2024

@author: ADMINIS
"""

x = int(input("Nhập vào số xe của bạn (gồm 4 chữ số): "))
if x >= 1000 and x < 10000:
    a = x//1000
    b = (x%1000)//100
    c = (x%100)//10
    d = x%10
    y = a+b+c+d
    print("Số nút ở số xe của bạn =", y%10)
else:
    print("Số xe không hợp lệ")