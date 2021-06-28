n=int(input())
i=0
ch=False
while i<=n:
    if n==2**i:
        ch=True
    i+=1
if ch:
    print("YES")
else:
    print("NO")
    
    
