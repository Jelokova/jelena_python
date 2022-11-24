sample=[(3,4,5),(2,4,5),(1,8,4)]
sample.sort()
print(sample)

sample.sort(key=lambda x: x[2])
print(sample)