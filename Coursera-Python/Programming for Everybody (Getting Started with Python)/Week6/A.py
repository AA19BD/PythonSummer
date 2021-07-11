def computepay(h, r):
    if h<=40:
        pay=h*r
        return pay
    elif h>40:
        above=h-40
        pay=(h-above)*r+(above*1.5*r)
        return pay
    
    
hrs = input("Enter Hours:")
rp=input("Enter Rate:")
try:
    flt_hrs=float(hrs)
    flt_rp=float(rp)
except:
    print("Error,enter numeric number!")
    quit()

p = computepay(flt_hrs, flt_rp)
print("Pay", p)