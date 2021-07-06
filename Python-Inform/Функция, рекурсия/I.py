from math import *
a=int(input())

check=0
def MinDivisor(a):
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            return i
    return a
            
print(MinDivisor(a))
    