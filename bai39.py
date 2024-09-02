# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:34:08 2024

@author: ADMINIS
"""

N = int(input("Nhập số nguyên n: "))
while N <= 0:
    N = int(input("Nhập số nguyên n: "))
S = 0
for i in range(1, N+1):
    S += (1/i)
print("Kết quả =", S)