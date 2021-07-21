import json

data ='''
{
    "name": "Bob",
    "phone":{
        "type":"intl",
        "number":"+112"
    },
    "email":{
        "hide":"yes"
    }
}
'''
info=json.loads(data)
print('Name',info['name'])
print('Phone number',info['phone']['number'])
print('Email',info['email']['hide'])