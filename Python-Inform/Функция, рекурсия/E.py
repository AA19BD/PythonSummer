from math import *
x=float(input())
y=float(input())
Xc=float(input())
Yc=float(input())
r=float(input())

def IsPointInCircle(x,y,Xc,Yc,r):
    return (x-Xc)**2+(y-Yc)**2<=r*r

if IsPointInCircle(x,y,Xc,Yc,r):
    print("YES")
else:
    print("NO")