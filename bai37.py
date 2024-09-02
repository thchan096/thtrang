# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:11:13 2024

@author: ADMINIS
"""

N = int(input("Nhập số n chẵn và lớn hơn 0: "))
while N <= 0 or N%2 != 0:
    N = int(input("Nhập số n nguyên và lớn hơn 0: "))
S = 0
for i in range(2, N+1, 2):
    S += i
print("Kết quả =", S)