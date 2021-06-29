prev=int(input())
sum=0
check=1
while check:
    next=int(input())
    if prev==0 and next==0:
        check=0
    else:
        sum+=prev
    prev=next
    
print(sum,sep=" ")

