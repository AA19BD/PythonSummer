x=int(input())
y=int(input())
x1=int(input())
y1=int(input())
if x==x1+1 and y==y1+2 or x==x1-1 and y==y1+2 or x==x1-1 and y==y1-2 or x==x1+1 and y==y1-2 or x==x1-2 and y==y1+1 or x==x1+2 and y==y1+1 or  x==x1+2 and y==y1-1 or  x==x1-2 and y==y1-1:
    print("YES")
else:
    print("NO")