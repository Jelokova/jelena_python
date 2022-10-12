import csv
with open('test.csv','r') as file:
    csv_reader=csv.reader(file) #read only once!
    next(csv_reader) #remove header or set header as header=  next(csv_reader), print=heaater
    # print(csv_reader)
    # print(list(csv_reader))
    for line in csv_reader:
        print(line)
    with open('test_copy.csv','w') as wfile:
        csv_writer=csv.writer(wfile, lineterminator='\n',delimiter='-') #lineterminator-конец строки
        csv_writer.writerows(csv_reader)
        #или Записали построчно в новый файл
        # for line in csv_reader:
        #     csv_writer.writerow(line)
with open('test_copy.csv','r')as file:
    data=csv.reader(file,delimiter='-')
    for line in data:
        print(line)