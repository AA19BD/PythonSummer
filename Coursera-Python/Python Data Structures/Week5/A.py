name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts=dict()
for line in handle:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    line=line.split()
    emails=line[1]
    for email in emails.split():
        counts[email]=counts.get(email,0)+1
 
MaxWord=None
MaxCount=None 
for key,value in counts.items():
    if MaxCount is None or value>MaxCount:
        MaxCount=value
        MaxWord=key
    
print(MaxWord,MaxCount)
