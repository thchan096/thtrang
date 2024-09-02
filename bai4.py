# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:35:05 2024

@author: ADMINIS
"""

x = int(input("Nhập vào số nguyên dương có 2 chữ số: "))
if 10 <= x and x <= 99:
    a = x//10
    b = x%10
    print("Tổng các chữ số: ",a+b)
else:
    print("Không xác định")
