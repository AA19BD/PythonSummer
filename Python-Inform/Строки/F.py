s=input()
count=len(s)-len(s.replace('f',''))
if count==1:
    print(-1)
elif count>=2:
    print(s.index('f',s.find('f')+1))
else:
    print(-2)