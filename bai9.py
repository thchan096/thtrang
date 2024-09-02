# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:13:45 2024

@author: ADMINIS
"""

print("============ MENU ============")
print("1. Hu tieu\n2. Chao long\n3. Banh canh\n4. Bun rieu\n5. Pho bo")
print("==============================")
chon = int(input("Moi nhap lua chon: "))
print("==============================")
if chon ==  1:
    print("Ban da chon Hu tieu")
elif chon == 2:
    print("Ban da chon Chao long")
elif chon == 3:
    print("Ban da chon Banh canh")
elif chon == 4:
    print("Ban da chon Bun rieu")
elif chon == 5:
    print("Ban da chon Pho bo")
else:
    print("Lua chon khong hop le")