largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number=int(num)
    except:
        print("Invalid input")
        continue
    if largest is None and smallest is None:
        largest=number
        smallest=number
    elif number>largest:
        largest=number
    elif number<smallest:
        smallest=number 
print("Maximum is",largest)
print("Minimum is",smallest)