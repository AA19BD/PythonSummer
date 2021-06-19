a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a==c and b!=d or a!=c and b==d or abs(a-c) == abs(b - d):
    print("YES")
else:
    print("NO")