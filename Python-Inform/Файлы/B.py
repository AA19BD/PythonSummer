input=open('input.txt','r')
output=open('output.txt', 'w')

s=input.read()
l=s.split()
sum=0
for i in l:
    sum+=int(i)
output.write(str(sum))

input.close()
output.close()