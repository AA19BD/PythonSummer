from math import *
a=float(input())
b=float(input())
c=float(input())
d=float(input())

def distance(a,b,c,d):
    return sqrt((a-c)**2+(b-d)**2)
print(distance(a,b,c,d))