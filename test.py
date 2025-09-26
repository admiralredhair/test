def summator(a, b):
    return a + b


print(summator(5, 10))


def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    

print(fact(5))