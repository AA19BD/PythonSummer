s=input()
s1=s.find('h')
s2=s.rfind('h')
s_new=s[s1+1:s2]
print(s[:s2]+s_new+s[s2:])