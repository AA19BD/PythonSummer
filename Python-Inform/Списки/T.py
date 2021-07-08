l=list(map(int,input().split()))
check=0
for i in range(len(l)):
    for j in range(len(l)):
        if i!=j and l[i]==l[j]:
            break
    else:
        print(l[i],end=" ")
