"""
LRU Cache
2. Using @lru_cache
ref: https://realpython.com/lru-cache-python/
"""
import time
from functools import lru_cache


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=128)
def fib_lru(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print('single time')
begin = time.time()
fib(30)
end = time.time()
print('general fib:', end-begin)
begin = time.time()
fib_lru(30)
end = time.time()
print('lru fib:', end-begin, '\n')

print('double times')
begin = time.time()
fib(31)
fib(31)
end = time.time()
print('general fib:', end-begin)
begin = time.time()
fib_lru(31)
fib_lru(31)
end = time.time()
print('lru fib:', end-begin, '\n')

print('triple times')
begin = time.time()
fib(32)
fib(32)
fib(32)
end = time.time()
print('general fib:', end-begin)
begin = time.time()
fib_lru(32)
fib_lru(32)
fib_lru(32)
end = time.time()
print('lru fib:', end-begin, '\n')
