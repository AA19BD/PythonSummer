n=int(input())
sum=0

for i in range(2,n+1):
    print("{}*{}".format((i-1),i),end="+" if i < n else "=")
    sum+=((i-1)*i)
print(sum)
