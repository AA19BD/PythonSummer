l=list(map(int,input().split()))
k=int(input())

def Delete_element(k):
    for i in range(k,len(l)):
        l.pop()
    return l

print(Delete_element(k))