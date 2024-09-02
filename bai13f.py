# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:14:06 2024

@author: ADMINIS
"""

a = int(input("Nhập vào ngày sinh của bạn: "))
b = int(input("Nhập vào tháng sinh của bạn: "))
c = int(input("Nhập vào năm sinh của bạn: "))
if a >= 1 and a <= 31 and b >= 1 and b <= 12:
    print(f"Năm, tháng, ngày sinh của bạn là: {c}/{b}/{a}")
else:
    print("Không xác định")