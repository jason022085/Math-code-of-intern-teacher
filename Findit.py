# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:11:28 2019

@author: USER
"""
#%%
def locat1(n,B,L,a,b):
    import math as m
    S = input("請輸入locat:")
    S = list(S)
   
    for i in S:
        locat = i
        if locat == "R" and n == B:
            a = m.ceil(a + (b-a)/2)
            b = b
            print("陽性樣本在",a,"和",b,"之間")
        if locat == "L" and n == B:
            a = a
            b = m.floor(a+(b-a)/2)
            print("陽性樣本在",a,"和",b,"之間")
        if locat == "R" and n != B:
            a = pow(2,m.floor(m.log2(b-a)))+a
            b = b
            print("陽性樣本在",a,"和",b,"之間")
        if locat == "L" and n != B:
            a = a
            b = pow(2,m.floor(log2(b-a)))+a-1
            print("陽性樣本在",a,"和",b,"之間")

    print("陽性在原數列的第",a,"項")   
#%%
def locat2(n,B,L,a,b):
    import math as m
    S = input("請輸入locat:")
    S = list(S)
   
    for i in S:
        locat = i
        if locat == "R" and n == B:
            a = m.ceil(a + (b-a)/2)
            b = b
            print("陽性樣本在",a,"和",b,"之間")
        if locat == "L" and n == B:
            a = a
            b = m.floor(a+(b-a)/2)
            print("陽性樣本在",a,"和",b,"之間")
        if locat == "R" and n != B:
            a = pow(2,m.floor(m.log2(b-a)))+a
            b = b
            print("陽性樣本在",a,"和",b,"之間")
        if locat == "L" and n != B:
            a = a
            b = pow(2,m.floor(log2(b-a)))+a-1
            print("陽性樣本在",a,"和",b,"之間")

    print("陽性在原數列的第",a,"項")   
#%%
def keyin():    
    n = input("請輸入樣本總數:")
    n = int(n)
    a = 1
    b = n
    if n == 0 or n == 1:
        B = 0
        L = 0        
        #如果n太小，k值會變0或負的，big2和lit2會變無意義，所以這邊拉出來定義
    else:
        for i in range(n):
            if pow(2,i) <= n and n < pow(2,i+1):
                k = i 
                B = pow(2,k)#B
                L = pow(2,k-1)#L  
    return n,B,L,a,b
#%%

n,B,L,a,b = keyin()
print('\n')
print("開始找第一個陽性的位置:")
locat1(n,B,L,a,b)
print('\n')
print("開始找第二個陽性的位置:")
locat2(n,B,L,a,b)
over = input("輸入任何鍵以結束程式")             