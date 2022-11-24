# def norm_fibonacci(number):
#     fibs=[0,1]
#     for i in range(2,number+1):
#         fibs.append(fibs[-1]+fibs[-2])
#     return fibs
# normal_fibs=norm_fibonacci(10)
# print(normal_fibs)
##############################
# def generator_fibonacci(number):
#     x2=0
#     x1=1
#
#     yield x2
#     yield x1
#     for item in range(2,number+1):
#         yield x2+x1
#         x2,x1 =x1, x2+x1
# gen_fiba=generator_fibonacci(10)
# print(next(gen_fiba))
# print(next(gen_fiba))
# print(next(gen_fiba))
# print(next(gen_fiba))
# print(next(gen_fiba))

##############
def inf_fibonacci():
    x2=0
    x1=1
    yield x2
    yield x1

    while True:
        yield x2+x1
        x2,x1=x1, x2+x1
inf_fibs= inf_fibonacci()
for range in range(100):
    print(next(inf_fibs))
