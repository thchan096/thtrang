# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:22:39 2024

@author: ADMINIS
"""

N = int(input("Nhập số n lẻ và lớn hơn 0: "))
while N <= 0 or N%2 == 0:
    N = int(input("Nhập số n nguyên và lớn hơn 0: "))
S = 1
for i in range(1, N+1):
    if N == 1:
        print("Kết quả = 1")
    elif N > 1:
        S *= i
print("Kết quả =", S) 