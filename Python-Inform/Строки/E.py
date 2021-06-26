s=input()
count=len(s)-len(s.replace("f",""))
if count==1:
    print(s.index("f"))
elif count>=2:
    print(s.index("f"),s.rindex("f"))
    
# if (s).count("f")>=2:
#     print(s.find("f"),s.rfind("f"))
# elif (s).count('f')==1:
#     print(s.find("f"))

