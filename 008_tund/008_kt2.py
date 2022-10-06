#total qty of word
with open("files/homework.txt", "r", encoding="utf-8") as file:
    data = file.read()
    total_qty = len(data.split())
    print(f'Общее кол-во слов:', total_qty)

#create list of words & remove waste symbols
with open("files/homework.txt", "r", encoding="utf-8") as file:
    data = file.read()
    data = data.replace("\n", " ")
    data = data.replace(",", "").replace(".", "").replace("?", "").replace("!", "")\
        .replace("(", "").replace(")", "").replace(":", "").replace("\"", "")
    data = data.lower()
    #print(data)
    worlds=data.split()
    #print(worlds)
    #print(type(worlds))

#create unique dictionary and counter
unique = {}
for world in worlds:
    if world in unique:
        unique[world] += 1
        continue
    else:
        unique.update({world: 1})
#print(unique)
#print(type(unique))

for k,v in sorted(unique.items()):
    print('{}: {}'.format(k,v))

