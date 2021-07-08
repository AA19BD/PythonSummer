l=list(map(int,input().split()))
min=1e10
for i in range(len(l)):
    if l[i]>0 and l[i]<min:
        min=l[i]
print(min)