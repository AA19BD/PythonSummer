l=list(map(int,input().split()))

for i in range(1,len(l),2):
    l[i-1],l[i]=l[i],l[i-1]
    
print(*l)#1

# for i in l:#2
#     print(i,end=" ")