def F(n):
    if n in (1,2):
        return 1
    else:
        return F(n-1)+F(n-2)
print(F(10))