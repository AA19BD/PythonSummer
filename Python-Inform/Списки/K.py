l=list(map(int,input().split()))
# l_set=set(l)
# print(len(l_set))
count=1
for i in range(1,len(l)):
    if l[i-1]!=l[i]:
        count+=1
print(count)
     