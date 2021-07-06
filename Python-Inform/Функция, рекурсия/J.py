from math import *
n=int(input())

def IsPrime(n):
    check=1
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return check==0
    return check

if IsPrime(n):
    print('YES')
else:
    print("NO")