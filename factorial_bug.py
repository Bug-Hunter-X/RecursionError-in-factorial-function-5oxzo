def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) #expect 120
print(factorial(-1)) #expect RecursionError