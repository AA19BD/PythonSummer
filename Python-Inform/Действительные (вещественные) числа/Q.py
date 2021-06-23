from math import *
n=int(input())
x=float(input())
sum=0
for i in range(0,n+1):
    sum+=pow(x,i)/(factorial(i))
print(sum)