# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:19:08 2024

@author: ADMINIS
"""

N = int(input("Nhập vào số N nguyên dương: "))
while N <= 0:
    N = int(input("Nhập lại số N nguyên dương: "))
for i in range(1, N+1):
    if N % i == 0:
        print("Ước số của", N, "là:", i)