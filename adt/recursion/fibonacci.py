def fibonacci(n):
    if n <= 1:
        return (0, n)
    else:
        (b, a) = fibonacci(n-1)
        return (a, a+b)


f = fibonacci(3)
print(str(f) + ' = ' + str(f[0] + f[1]))

