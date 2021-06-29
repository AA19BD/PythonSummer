check=1
max=-10e9
while check:
    a=int(input())
    if a==0:
        check=0
    else:
        if a>max:
            max=a
print(max)