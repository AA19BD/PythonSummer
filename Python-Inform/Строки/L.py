s=input()
s1=s.find('h')
s2=s.rfind('h')


s3=s[:s1+1]
s4=s[s2:]

s6=s[s1+1:s2]
s7=s6.replace('h',"H")
print(s3+s7+s4)