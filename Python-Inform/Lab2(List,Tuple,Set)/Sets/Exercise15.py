l=list(map(int,input().split()))

def Odd_Number_In_Even_Pos():
    for i in range(len(l)):
        if i%2==0 and l[i]%2!=0:
            return i
print(Odd_Number_In_Even_Pos())