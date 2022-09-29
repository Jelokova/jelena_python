def func_with_argument(a,b):
    return a**b
print(func_with_argument(2,3))

########
def func_devision(a,b):
    if a<b:
        return b-a
    if a > b:
        return a - b
print(func_devision(3,6))

###### function iside function
def double(num)
    return num*2
def four_times(num)
    x=double(double(num))
    return x
