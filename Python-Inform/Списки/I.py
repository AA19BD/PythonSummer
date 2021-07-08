l=list(map(int,input().split()))
min=0
check=False
for i in range(len(l)):
    if l[i]%2!=0:
        min=l[i]#находишь 1 нечетное,
        break

for i in range(len(l)):
    if l[i]%2!=0 and l[i]<min:
        min=l[i]
if min!=0:
    print(min)
else:
    print(0)
        
    

