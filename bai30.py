# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:04:20 2024

@author: ADMINIS
"""

thang = int(input("Nhập vào tháng (1-12): "))
while thang < 1 or thang > 12:
    thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập vào năm: "))
nam_nhuan = (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0
if nam_nhuan:
    print("Năm nhuận")
else:
    print("Năm không nhuận")
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng", thang, "năm", nam, "có 31 ngày")
elif thang in [4,6,9,11]:
    print("Tháng", thang, "năm", nam, "có 30 ngày")
else:
    if thang == 2:
        if nam_nhuan:
            print("Tháng 2", "năm", nam, "có 29 ngày")
        else:
            print("Tháng 2", "năm", nam, "có 28 ngày")