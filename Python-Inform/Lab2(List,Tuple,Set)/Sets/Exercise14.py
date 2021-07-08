l=list(map(int,input().split()))
k=int(input())
check=0
def More_than(k):
    l2=[]
    for i in range(len(l)):
        if l[i]>k:
            l2.append(l[i])
    return set(l2)

print(More_than(k))