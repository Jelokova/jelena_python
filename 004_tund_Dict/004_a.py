x=5
#dictionary #Key,value1,value2,
student={'name':'Jack', 'age': 32,'courses':['Match','Art','Programming'],
        1:'int_key', 0.2:'float_key', x:'variable','var_value': x, True:'hello world'}
print(student['name']) # index is key
print(student[x])
print(student.get('job')) #if key is not exisist, give None and programm will continue
print(student.get('job','key not found'))
print(student['courses'][2])
student['name']='John' #changed value
student['phone']='555-55-555' #added new key and value
print(student)
student.update({'name':'John', 'age': 27, 'phone':'4444-444-44'})
print(student)
del student['phone']
print(student)
age=student.pop('age')
print(age)
print(student)

print(student)
print(len(student))
for x in student:
        print()