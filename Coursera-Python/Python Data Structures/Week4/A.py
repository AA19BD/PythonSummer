fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    line=line.split()
    for i in line:
        if i in lst:
            continue
        else:
            lst.append(i)
            lst.sort()
print(lst)
        



 
    
 
