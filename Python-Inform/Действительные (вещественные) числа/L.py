a = float(input())
b = float(input())
c = float(input())
D = ((b) ** 2) - (4 * a * c)
if a == 0:
    if b == 0 and c == 0:
        print(3)
    if b != 0 and (c != 0 or c == 0):
        x = -(c / b)
        print(1,x)
    if b==0 and c!=0:
        print(0)
else:
    if D > 0:
        x1 = ((-b) - (D ** 0.5)) / (2 * a)
        x2 = ((-b) + (D ** 0.5)) / (2 * a)
        if x1 < x2:
            x2, x1 = x1, x2
        print(2,x2,x1)
    elif D == 0:
        x = (-b) / (2 * a)
        print(1,x)
    elif D < 0:
        print(0)