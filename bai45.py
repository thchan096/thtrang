# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:02:04 2024

@author: ADMINIS
"""

N = int(input("Nhập số nguyên n: "))
x = float(input("Nhập số nguyên x: "))
while N <= 0:
    N = int(input("Nhập số nguyên n: "))
S = x
for i in range(2, N+1):
    S+=((x**i)/((i*(i+1))//2))
print("S =", S)