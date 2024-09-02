# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:07:08 2024

@author: ADMINIS
"""

N = int(input("Nhập số n nguyên và lớn hơn 0: "))
while N <= 0:
    N = int(input("Nhập số n nguyên và lớn hơn 0: "))
S = 0
for i in range(1, N+1):
    S += i**2
print("Kết quả =", S)