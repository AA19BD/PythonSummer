a=int(input())
b=int(input())

def sum(a,b):
    # a+=1
    # b-=1
    if b>0:
        return sum(a+1,b-1)
    else:
        return a
        
print(sum(a,b))