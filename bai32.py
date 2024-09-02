# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:02:41 2024

@author: ADMINIS
"""

x = int(input("Quãng đường khách đi được trên taxi (km): "))
if 2 <= x <=5:
    print("Phí đi taxi (đ):", 15 + 13.5*(x-1))
elif 6 <= x < 120:
    print("Phí đi taxi (đ):", 15 + (13.5*4)+11*(x-5))
elif x <= 1:
    print("Phí đi taxi (đ):", 15*x)
else:
    print("Phí đi taxi (đ):", (15 +(13.5*4)+11*(x-5))*0.9)