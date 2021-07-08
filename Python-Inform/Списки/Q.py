l=list(map(int,input().split()))
k=int(input())
for i in range(k+1,len(l)):
    l[i-1]=l[i]
l.pop()

print(*l)