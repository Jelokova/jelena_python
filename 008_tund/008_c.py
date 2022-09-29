with open("files/lorem.txt", 'r', encoding="utf-8") as file:
    chunk = 100
    data =file.read(chunk) #читвть кусочками
    while len(data)>0:
        print(data)
        data=file.read(chunk)