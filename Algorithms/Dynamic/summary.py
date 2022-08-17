import time

# In a data structure, dynamic allocation means while executing a program, allocating a necessary memory
# When to use?
# 1. Optimal Substructure
# Break down a big problem to small problems
# 2. Overlapping Subproblem
# Identical same problems -> repeatedly solve


def fib(n):
    # a(n) = a(n-1) + a(n-2), a(1) = 1, a(2) = 1
    # problem: f(x) is called several times, Big O: O(2^N)
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


start = time.time()
print(fib(30))
end = time.time()
print('Processing time(Recursive):', end-start, '\n')

# Memoization: one of implements in dynamic programming
# Memorize the result of execution result to a memory space
# Upon calling the same problem, bring the memorized result
# == Caching

# Initialize the list to memo the result of one execution
d = [0] * 1000


def fib2(n):
    # Top-down
    # O(N)
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fib2(n - 1) + fib2(n - 2)
    return d[n]


start = time.time()
print(fib2(999))
end = time.time()
print('Processing time(Top-down):', end-start, '\n')


d[1] = 1
d[2] = 1


def fib3(n):
    # Bottom-up
    # O(N)
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n]


start = time.time()
print(fib3(999))
end = time.time()
print('Processing time(Bottom-up):', end-start)
