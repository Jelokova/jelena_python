import csv
with open('2019.csv','r',encoding='utf8') as file:
    csv_data=list(csv.DictReader(file))
   #
result_list=[]
for line in csv_data:
    result_list.append([line['GDP per capita'], line['Overall rank'], line['Country or region']])
result_list.sort()
#print(result_list)
top_list=[]
while len(top_list)<10:
    top_list.append(result_list.pop())
for x in top_list:
    print(x)