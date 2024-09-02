# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:58:35 2024

@author: ADMINIS
"""

N = int(input("Nhập số nguyên n: "))
while N <= 0:
    N = int(input("Nhập số n nguyên và lớn hơn 0: "))
S = 0
for i in range(1, N+1):
    S += (1/(i*(i+1)))
print("Kết quả =", S)