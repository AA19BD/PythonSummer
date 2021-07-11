sum=0
count=0
while True:
    number=input("Enter a number:")
    if number=='done':
        break
    try:
        n=float(number)
    except:
        print("Invalid input")
        continue
    sum+=n
    count+=1
  
print(sum,count,sum/count)
    
    