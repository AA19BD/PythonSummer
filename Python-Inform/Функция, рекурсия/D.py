from math import *
a=float(input())
b=float(input())

def IsPointInSqure(a,b):
    return -1<=a<=1 and -(0.5)<=b<=(0.5) or (a==0 and -1<=b<=1)

if IsPointInSqure(a,b):
    print("YES")
else:
    print("NO")