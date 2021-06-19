a=int(input())
a1=(a//10)//100 #2002//100=20(first 2)
a2=a%10 #2002%10=2(last 2)
b1=((a//10)%100)%10
b2=(a%1000)//100
if a1==a2 and b1==b2:
    print(1)
else:
    print(3)