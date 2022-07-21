# Should define an exit point

# Fibonacci
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


# Euclidean Algorithm
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(fib(10))
print(gcd(192, 162))
