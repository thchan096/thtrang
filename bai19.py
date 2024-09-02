# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:00:56 2024

@author: ADMINIS
"""

a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
d = int(input("Nhập vào số nguyên d: "))
if a<b and a<c and a<d:
    print("Số nhỏ nhất là", a)
elif b<a and b<c and b<d:
    print("Số nhỏ nhất là", b)
elif c<a and c<b and c<d:
    print("Số nhỏ nhất là", c)
else:
    print("Số nhỏ nhất là", d)
        
    