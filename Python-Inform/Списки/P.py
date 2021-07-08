l=list(map(int,input().split()))
index_min=0
index_max=0

for i in range(len(l)):
    if l[i]>l[index_max]:
        index_max=i
    if l[i]<l[index_min]:
        index_min=i
l[index_max],l[index_min]=l[index_min],l[index_max]
print(*l)
    
    