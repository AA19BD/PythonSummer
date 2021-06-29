check=1
count=0
while check:
    a=int(input())
    if a==0:
        check=0
    else:
        if a%2==0:
            count+=1

print(count)
            