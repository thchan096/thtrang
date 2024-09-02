# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:40:53 2024

@author: ADMINIS
"""

a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
if a>b and b>c:
    print(f"Thứ tự tăng dần các số:\t {a}\t {b}\t {c}")
elif a>c and c>b:
    print(f"Thứ tự tăng dần các số:\t {a}\t {c}\t {b}")
elif b>a and a>c:
    print(f"Thứ tự tăng dần các số:\t {b}\t {a}\t {c}")
elif b>c and c>a:
    print("Thứ tự tăng dần các số:\t {b}\t {c}\t {a}")
elif c>b and b>a:
    print("Thứ tự tăng dần các số:\t {c}\t {b}\t {a}")
else:
    print("Thứ tự tăng dần các số:\t {c}\t {a}\t {b}")