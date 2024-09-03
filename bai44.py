# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:01:09 2024

@author: ADMINIS
"""

N = int(input("Nhập số nguyên n: "))
while N <= 0:
    N = int(input("Nhập số nguyên n: "))
S = 0
for i in range(0, N+1):
    S+=(((2*i)+1)/((2*i)+2))
print("S =", S)