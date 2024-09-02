# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:24:11 2024

@author: ADMINIS
"""

print("1. Hinh chu nhat\n2. Hinh vuong\n3. Hinh tron")
hinh = int(input("Tính diện tích và chu vi của: "))
if hinh == 1:
    a = int(input("Nhập vào chiều dài hình chữ nhật: "))
    b = int(input("Nhập vào chiều rộng hình chữ nhật: "))
    print("Diện tích của hình chữ nhật =", a*b)
    print("Chu vi của hình chữ nhật =", (a+b)*2)
elif hinh == 2:
    a = int(input("Nhập vào độ dài cạnh hình vuông: "))
    print("Diện tích của hình vuông =", a*a)
    print("Chu vi của hình vuông =", a*4)
elif hinh == 3:
    a = int(input("Nhập vào bán kính hình tròn: "))
    print("Diện tích của hình tròn =", a*a*3.14)
    print("Chu vi của hình tròn =", a*2*3.14)
else:
    print("Không xác định")