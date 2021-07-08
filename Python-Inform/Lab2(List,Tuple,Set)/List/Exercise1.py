l=list(map(int,input().split()))
k=int(input())

def Index(k):
    for i in range(len(l)):
        if i==k:
            return l[i]
    




print(Index(k))