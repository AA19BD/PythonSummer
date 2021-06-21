a=int(input())
b=int(input())
c=int(input())
d=int(input())
# ch=False
# for i in range(a,b+1):
#     if i%d==c:
#         print(i,end=" ")
start=(a-c+d-1)//d*d+c
for i in range(start, b + 1, d):
    print(i, end = ' ')