fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    line=line.split()
    word=line[1]
    count+=1
    print(word)
  
print("There were", count, "lines in the file with From as the first word")
