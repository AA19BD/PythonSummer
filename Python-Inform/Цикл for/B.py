a=int(input())
b=int(input())
def Increase(*args):
    for i in range(a,b+1):
        print(i,end=" ")
def Decrease(*args):
    for i in range(a,b-1,-1):
        print(i,end=" ")
if a<b:
    Increase(a,b)
else:
    Decrease(a,b)
    
