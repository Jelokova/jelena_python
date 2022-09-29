# 'r'='read'
# 'a'='append'
# 'w'='write'
# 'x'='create'
# 'r+'='read and write'


#C:\Users\gamma\PycharmProjects\jelena_python\007_tund\007_a.py
#007_tund/007_a.py
with open("files/lorem.txt", 'r', encoding="utf-8") as file:
    #внутри конструкции файл открыт.

# encodung for EST cp1252 or cp1257
    print(file.name)
    print(file.encoding)
    print(file.closed)
    file.close()
    print(file.closed)

with open("files/lorem.txt", 'r', encoding="utf-8") as file:
    #data = file.read()
    # print(data)
    # data=file.readlines()
    # for line in data:
    #     print(line)

    data=file.readline(30)
    print(data)
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)


