# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:20:31 2024

@author: ADMINIS
"""

a = int(input("Nhập vào ngày sinh của bạn: "))
b = int(input("Nhập vào tháng sinh của bạn: "))
c = int(input("Nhập vào năm sinh của bạn: "))
if a >= 1 and a <= 31 and b >= 1 and b <= 12:
    c = str(c)[-2:]
    print(f"Ngày, tháng, năm sinh của bạn là: {a}/{b}/{c}",)
else:
    print("Không xác định")