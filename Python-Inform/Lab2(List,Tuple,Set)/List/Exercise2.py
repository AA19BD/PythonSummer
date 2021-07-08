l=list(map(int,input().split()))

def Even_values():
    for i in range(len(l)):
        if i%2==0:
            print(l[i],end=" ")
    
        
Even_values()