sh=input("Enter hours:")
sr=input("Enter Rate:")
try:
    fh=float(sh)
    fr=float(sr)
except:
    print("Error,please print numeric input")
    quit()
    
print(fh,fr)
if fh>40:
    reg=fr*fh
    otp=(fh-40)*(fr*0.5)
    xp=reg+otp
else:
    xp=fr*fh
print("Pay:",xp)
    