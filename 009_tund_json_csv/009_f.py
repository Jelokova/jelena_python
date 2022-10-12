import csv
with open('test.csv','r') as file:
    csv_reader = csv.DictReader(file)

    with open('test_copy2.csv','w') as wfile:
        fn=['Name','Date of birth','Town']
        csv_writer=csv.DictWriter(wfile, fieldnames=fn,lineterminator='\n')
        for line in csv_reader:
            csv_writer.writerow(line)
        print(csv_writer)
