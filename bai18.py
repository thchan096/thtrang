# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:54:33 2024

@author: ADMINIS
"""

x1 = int(input("Nhập giờ của thời gian thứ nhất: "))
y1 = int(input("Nhập phút của thời gian thứ nhất: "))
z1 = int(input("Nhập giây của thời gian thứ nhất: "))
x2 = int(input("Nhập giờ của thời gian thứ hai: "))
y2 = int(input("Nhập phút của thời gian thứ hai: "))
z2 = int(input("Nhập giây của thời gian thứ hai: "))
a = x1+y1+z1
b = x2+y2+z2
print("Tổng hai thời gian:", a+b)
print("Hiệu hai thời gian:", a-b)