l=list(map(int,input().split()))
index=0
c=0
for i in range(len(l)):
    if l[i]>l[index]:
        index=i
print(l[index],index,sep=" ")

# for index,i in enumerate(l):
#     if i>max:
#         max,c=i,index
    
# print(max,c)
        