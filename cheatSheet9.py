    # web services (xml) (json)

    # json

import json

data = '''
{
  "name" : "Hesham",
  "phone" : {
    "type" : "intl",
    "number" : "+201111111111"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)

print('\nName:', info["name"])
print('Hide:', info["email"]["hide"])

print('\n------------------------------\n')

    # dic within a list 

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

print('\n------------------------------\n')
