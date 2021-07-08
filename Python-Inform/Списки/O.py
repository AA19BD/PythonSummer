l=list(map(int,input().split()))
l2=[]
l2.insert(0,l.pop())
l2.extend(l)
print(*l2)

    