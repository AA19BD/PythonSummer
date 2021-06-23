a=float(input())
seconds=(a*60)/30*60
hours=(seconds//60)//60
minute=(seconds//60)%60
second=seconds%60
print(int(hours),int(minute),int(second),sep=" ")
