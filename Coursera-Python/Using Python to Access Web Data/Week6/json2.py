import json 

input='''
[
    {
        "id": "001",
        "x":"2",
        "name": "Bob"
        
    },
    {
        "id": "002",
        "x":"3",
        "name": "Clark"
        
    }
]
'''
info =json.loads(input)#list 
print("User count:",len(info))
for item in info:
    print('Users Id -',item['id'])
    print("Users name -",item['name'])
    print("Attribute -",item['x'])