x=float(input())
y=float(input())

def IsPointSquare(a,b):
    return -1<=(a)<=1 and -1<=b<=1

if IsPointSquare(x,y):
    print("YES")
else:
    print("NO")
