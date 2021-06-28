n= int(input())
if n!= 2 and n% 2 :
    i = 3
    while i*i<=n:
        if n%i == 0 :
            n=i
            break
        i += 2
else:
    n=2
print(n)