# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("Error of file name",fname)
    quit()
    
for line in fh:
    line=line.rstrip()
    print(line.upper())
    
    