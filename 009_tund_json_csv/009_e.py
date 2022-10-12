import csv
with open('test.csv','r') as file:
    csv_reader = csv.DictReader(file) #fildnames=headers)
    print(csv_reader)
    for line in csv_reader:
        print(line)
