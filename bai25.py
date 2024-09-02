# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:37:33 2024

@author: ADMINIS
"""

y = input("Nhập một chữ cái: ")
if y.islower():
    print("Chữ cái sau khi chuyển đổi:", y.upper())
elif y.isupper():
    print("Chữ cái sau khi chuyển đổi:", y.lower())
else:
    print("Đây không phải là một chữ cái")