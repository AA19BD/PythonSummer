count=0
sum=0
check=True
while check:
    a=int(input())
    if a==0:
        check=False
    else:
        count+=1
        sum+=a
    av=sum/count
print(av)