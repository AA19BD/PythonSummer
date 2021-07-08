l=list(map(int,input().split()))


def Set_with_Neighnor():
    l2=[]
    for i in range(len(l)):
        l[i]=l[i]-1
        l2.append(l[i])
        l[i]=l[i]+2
        l2.append(l[i])
    return l2
        
print(set(Set_with_Neighnor()))
        