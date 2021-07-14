input=open('input.txt','r')
output=open('output.txt', 'w')
sum=0
for line in input:
    line=line.rstrip()
    sum+=int(line)
    
output.write(str(sum))

input.close()
output.close()