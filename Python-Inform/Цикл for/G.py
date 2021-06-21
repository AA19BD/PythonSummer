n=int(input())
k=int(input())

def Factorial(a):
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact
        
print(Factorial(n)//(Factorial(k)*Factorial(n-k)))