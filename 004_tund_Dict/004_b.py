x=5
#dictionary #Key,value1,value2,
student={'name':'Jack', 'age': 32,'courses':['Match','Art','Programming'],
        1:'int_key', 0.2:'float_key', x:'variable','var_value': x, True:'hello world'}
for x in student:
    print(x)

for y in student.values():
    print(y)

print(student.keys())
print(student.values())
print(student.items())