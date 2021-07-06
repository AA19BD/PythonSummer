def Summa(a):
    n=int(input())
    if n!=0:
        return Summa(a+n)
    return a
print(Summa(0))