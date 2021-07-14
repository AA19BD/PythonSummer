input=open('input.txt','r')
output=open('output.txt', 'w')

for line in input:
    line=line.rstrip()
    output.write(str(line[::-1]))

    
input.close()
output.close()