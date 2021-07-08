l1=set(map(int,input().split()))
l2=set(map(int,input().split()))

def Differce_in_set(l1,l2):
    return l1.difference(l2)
print((Differce_in_set(l1,l2)))