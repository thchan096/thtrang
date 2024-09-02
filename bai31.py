# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:23:07 2024

@author: ADMINIS
"""

a = float(input("Nhập vào số a nguyên dương: "))
b = float(input("Nhập vào số b nguyên dương: "))
c = float(input("Nhập vào số c nguyên dương: "))
if a+b > c or a+c > b or b+c > a:
    if a == b or b == c or a == c:
        print("Tam giac abc là tam giac can")
    if a == b == c:
        print("Tam giac abc là tam giac deu")
    if a*a + b*b == c*c:
        print("Tam giac abc là tam giac vuong")
    else:
        print("Tam giac abc là tam giac thuong")
else:
    print("Không phai la 3 canh của tam giac")