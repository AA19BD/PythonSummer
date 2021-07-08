l=list(map(int,input().split()))
x=int(input())
x_index=0
for i in range(len(l)):
    if l[i]>=x:
        x_index+=1
    
print(x_index+1)