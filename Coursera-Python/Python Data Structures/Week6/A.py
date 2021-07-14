name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

di=dict()

for line in handle:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        words=line.split()
        whole_time=words[5]
        time=whole_time.split(':')
        first_hour=time[0]
        for hour in first_hour.split():
            di[hour]=di.get(hour,0)+1

# lst=[]----For sorting in value-key pair
# for k,v in di.items():
#     value_key=(v,k)
#     lst.append(value_key)
# lst=sorted(lst)
# for v,k in lst:
#     print(k,v,sep=" ")

for k,v in sorted(di.items()):
    print(k,v)


        
