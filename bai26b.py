# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:54:08 2024

@author: ADMINIS
"""

N = int(input("Nhập vào 1 số nguyên N: "))
chuoi = str(N)
x = ''.join(sorted(chuoi))
y = int(x)
print("Các con số theo thứ tự tăng dần:", y)