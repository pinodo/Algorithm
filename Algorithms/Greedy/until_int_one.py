# Until a number(N) becomes 1, one of process will be continuously executed
# 1. Subtract N - 1
# 2. N / K
# Write a program that returns a minimum times until N becomes 1

# Idea
# Division first


# my answer
def func(n, k):
    if (1 <= n <= 100000) and (2 <= k <= 100000):
        result = 0
        while True:
            if n == 1:
                return result
            if n % k == 0:
                n //= k
            elif n % k != 0:
                n -= 1
            result += 1


# ex answer
def func2(n, k):
    result = 0
    while True:
        target = (n // k) * k
        result += (n - target)
        n = target
        if n < k:
            break
        result += 1
        n //= k
    result += (n - 1)
    return result


print(func(25, 3))
print(func2(25, 3))
