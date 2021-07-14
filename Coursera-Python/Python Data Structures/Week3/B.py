# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Error of name ",fname)
    quit()

general=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count+=1
    space_line=line.find(' ')
    number_line=line[space_line+1:]
    general+=float(number_line)
    
print("Average spam confidence:",general/count)

