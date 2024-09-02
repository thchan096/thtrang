# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:22:56 2024

@author: ADMINIS
"""

import math

print("Ta co phuong trinh: ax + b = 0")
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm (vì 0x + 0 = 0 luôn đúng)")
    else:
        print("Phương trình vô nghiệm (vì 0x + b = 0 với b ≠ 0 không thể xảy ra)")
else:
    x = -b / a
    print(f"Phương trình có một nghiệm duy nhất: x = {x}")