
    #args = unlimited qty arguments ,create cartage
    #kwargs = unlimited qty argumets with key
import my_functions
from my_functions import volume

def tester(a,b,c=1):
    return a+b+c

def sum_numbers(*args):
    res =0
    for num in args:
        res += num
    return res

def tester2(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')
emp_dict ={'name':'Jack','surname':'Smith', 'age':34,'salary':2000}
tester2(**emp_dict)

print(my_functions.area(2,5))