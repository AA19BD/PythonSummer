a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print(3)
elif a==b!=c or a==c!=b or c==b!=a:
    print(2)
else:
    print(0)