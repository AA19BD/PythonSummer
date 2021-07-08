l=list(map(int,input().split()))
l2=[]
for i in range(len(l)):
    l2.append(l[i])
    
l2.reverse()  
print(" ".join(map(str,l2)))

#2
# l=list(map(int,input().split()))
# l2=[]

# for i in reversed(l):
#     print(i,end=" ")