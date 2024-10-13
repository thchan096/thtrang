# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
#BAI 52 LAB01
#1/a
def can_bac(n,x):
    return n**(1/x)

#1/b
def sodao(n):
    return str(n)[::-1] #chuoi, chu so
def so_dao(n):
    so_dao = 0
    while n>0:
        so_dao = so_dao*10 + n%10
        n //=10
    return so_dao

#1/c
def so_cp(n):
    return int(math.sqrt(n))**2 == n

#1/d
def so_ngto(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

#1/e
def tich_le(n):
    tich =1
    for i in str(n):
        if int(i)%2 !=0:
            tich *= int(i)
    return tich

#1/f
def tong_snt(n):
    tong_snt = 0
    for i in range(2,n):
        if so_ngto(i):
            tong_snt += i
    return tong_snt

#1/g
def tong_scp(n):
    tong_scp = 0
    for i in range(1,n):
        if so_cp(i):
            tong_scp += i
    return tong_scp

#1/h
def tong_uoc(n):
    tong_uoc = 0
    if n<=0:
        return False
    while n>0:
        for i in range(1,n+1):
            if n%i == 0:
                tong_uoc += i
        return tong_uoc


if __name__=="__main__":
    print(can_bac(3,7))
    print(sodao(450634))
    print(so_dao(456780))
    print(so_cp(4))
    print(so_ngto(10))
    print(tich_le(3275))
    print(tong_snt(14))
    print(tong_scp(16))
    print(tong_uoc(15))