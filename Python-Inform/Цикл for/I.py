n=int(input())

for i in range(1,n+1):
    print("+___",end=" ")
print()
for i in range(1,n+1):
    print("|{} /".format(i),end=" ")
print()
for i in range(1,n+1):
    print("|__\\",end=" ")
print()
for i in range(1,n+1):
    print("|   ",end=" ")