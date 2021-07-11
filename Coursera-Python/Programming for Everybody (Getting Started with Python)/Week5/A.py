hrs = input("Enter Hours:")
h = float(hrs)
r_per_hour=float(input("Enter Rate:"))

above_h=0
if h<=40:
    print(h*r_per_hour)
elif h>40:
    above_h=h-40
    print((h-above_h)*r_per_hour+above_h*1.5*r_per_hour)