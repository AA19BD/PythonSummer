from math import *
a=float(input())
b=float(input())
c=float(input())
d=(b**2)-(4*a*c)
x1=0
x2=0
x3=0
if d>0:
    x1+=(-b+sqrt(d))/(2*a)
    x2+=(-b-sqrt(d))/(2*a)
    if x1<x2:
        print((x1),(x2))
    else:
        print((x2),(x1))
elif d==0:
    x3+=(-b)/(2*a)
    print(x3)

    