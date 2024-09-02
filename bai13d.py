# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:01:55 2024

@author: ADMINIS
"""

a = int(input("Nhập vào năm sinh của bạn: "))
b = int(input("Nhập vào tháng sinh của bạn: "))
c = int(input("Nhập vào ngày sinh của bạn: "))
if c >= 1 and c <= 31 and b >= 1 and b <= 12:
    print(f"Ngày, tháng, năm của bạn là: {c}/{b}/{a}")
else:
    print("Không xác định")