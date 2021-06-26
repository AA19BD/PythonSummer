s=input()
s1=s.find('h')
s2=s.rfind('h')
s_new=s[s1:s2+1]
print(s[:s1]+s_new[::-1]+s[s2+1:])