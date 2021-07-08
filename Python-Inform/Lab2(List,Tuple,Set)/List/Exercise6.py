l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
i=int(input())
d=int(input())


def Insert_delete(i,d):
    l1.insert(i,l2)
    for i in range(d,len(l1)):
        x=l1.pop()
        
    return l1

print(Insert_delete(i,d))