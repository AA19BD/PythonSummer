l=list(map(int,input().split()))
check=False
for i in range(1,len(l)):
    if l[i]>l[i-1]:
        print(l[i],end=" ")

