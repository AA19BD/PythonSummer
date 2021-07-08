l=list(map(int,input().split()))

def Reversed_List():
    l2=[]
    for i in range(len(l)):
        x=l.pop()
        l2.append(x)
    return l2


def Reversed_List2():
    for i in reversed(l):
        print(i,end=" ")

def Reversed_List3():
    l2=[]
    for i in range(len(l)):
        l2.append(l[i])
        
    l2.reverse()  
    print(" ".join(map(str,l2)))

Reversed_List3()
