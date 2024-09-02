# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:36:02 2024

@author: ADMINIS
"""

x = float(input("Nhập giờ (h): "))
y = float(input("Nhập phút: "))
z = float(input("Nhập giây (s): "))
if (0 <= x <= 23) and (0 <= y <= 59) and (0 <= z <= 59):
    print("Thời gian hợp lệ")
else:
    print("Thời gian không hợp lệ")