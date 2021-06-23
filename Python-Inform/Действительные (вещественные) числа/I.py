p=int(input())
x=int(input())
y=int(input())
k=int(input())

summ_k=x*100+y

for i in range(k):
    summ_k+=int((summ_k*p)/100)

print((summ_k)//100,(summ_k)%100,sep=" ")

