# def square_list(numbers):
#     res=[]
#     for num in numbers:
#         res.append(num**2)
#     return res
# print(square_list([2,3,4]))
#************

# def area (a,b):
#     c=10 #variable inside function body see  first. if no - will check all code, but before activate function
#     return a*b*c
# print(area(1,1))
# c=5
# print(c)
##########################

def area(a,b):
    global c #global variable, can use utside function
    c.append([a,b])
    return c
c = []
area(1,2)
area(2,3)

print(c)