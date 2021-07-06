n=int(input())
k=int(input())

def C(n,k):
    if k==0:
        return 1
    elif k>n:
        return 0
    else:
        return C(n-1,k-1)+C(n-1,k)
    
print(C(n,k))