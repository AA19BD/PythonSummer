from math import *
p=float(input())
r=float(input())
k=float(input())

    
s=(r*100+k)#сумма общая с копейками
P=int(s*(p+100)/100)#размер влада через год
print((P//100),(P%100),sep=" ")
