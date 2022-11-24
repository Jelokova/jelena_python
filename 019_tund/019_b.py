def gen_squares(number):
    for i in range(1, number+1):
        yield i ** 2
generator_sq=gen_squares(10)
print('Generator squares!')
print(next(generator_sq))
print(next(generator_sq))
print(next(generator_sq))
