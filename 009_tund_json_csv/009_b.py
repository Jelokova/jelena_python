import json
with open('people.json','r') as file:
    data=json.load(file)
print(data)
for person in data['people']:
    if person ['has_licence']==False:
        del person ['has_licence']

with open ('people.json','w')as file:
    json.dump(data,file,indent=2)