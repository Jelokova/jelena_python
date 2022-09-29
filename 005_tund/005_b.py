def func_with_argument(num):
    return num ** 2
print(func_with_argument(4))
nums=[1,2,3,4,5,6,7,8,9,10]
for x in nums:
    print (func_with_argument(x))

for x in (range(100)):
    print (func_with_argument(x))
