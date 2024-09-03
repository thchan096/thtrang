# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:57:31 2024

@author: ADMINIS
"""

N = int(input("Nhập số nguyên n: "))
while N <= 0:
    N = int(input("Nhập số nguyên n: "))
S = 0
for i in range(1, N+1):
    S+=(i/(i+1))
print("S =", S)