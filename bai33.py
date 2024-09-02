# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:43:30 2024

@author: ADMINIS
"""

import math

N = int(input("Nhập số nguyên dương N: "))
while N<=0:
    N = int(input("Nhập lại số nguyên dương N: "))
if math.sqrt(N)**2 == N:
    print(f"{N} là số chính phương")
else:
    print(f"{N} không phải là số chính phương")