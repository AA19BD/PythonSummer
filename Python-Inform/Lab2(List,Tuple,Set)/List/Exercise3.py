l=list(map(int,input().split()))
k=int(input())

def Square_Values(k):
    l2=[]
    for i in range(k,len(l)):
        l2.append(l[i]**2)
    l3=l[:k]+l2
    return l3

        
def Square_Values2(k):
    for i in range(k,len(l)):
        a=l.pop(i)
        l.insert(i,int(a)**2)
    return l

print(Square_Values2(k))