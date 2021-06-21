a=int(input())
b=int(input())
for i in range(a,b+1):
    if int(str(i)[0])==int(str(i)[3]) and int(str(i)[1])==int(str(i)[2]):
        print(i)