from math import *
check=1
sum=0
sum1=0
count=0
double=0
s=0
while check:
    a=int(input())
    if a==0:
        check=0
    else:
        count+=1
        double+=(a**2)
        sum+=a
    s=sum/count  
print(sqrt((double-2*s*sum+count*s*s)/(count-1)))
    