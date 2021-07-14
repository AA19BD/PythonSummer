input=open('input.txt','r')
output=open('output.txt', 'w')

s=input.readlines()
s=s[::-1]
for i in s:
    output.write(i)


input.close()
output.close()