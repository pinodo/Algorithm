"""
LRU Cache
1. Using a Python Dictionary
ref: https://www.kunxi.org/2014/05/lru-cache-in-python/
"""
import time


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru = {}
        self.tm = 0

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm = self.tm + 1
            print('Cached ......')
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if len(self.cache) > self.capacity:
            old_key = min(self.lru.keys(), key=lambda k: self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        else:
            self.cache[key] = value
            self.lru[key] = self.tm
            self.tm = self.tm + 1

        print('LRU: {}'.format(self.lru))
        print('CACHE: {}'.format(self.cache))


if __name__ == '__main__':
    cache = LRUCache(capacity=10)
    cache.set('Name', 'Alvin')
    cache.set('Age', 28)
    cache.set('Job', 'Develop')


cache = LRUCache(capacity=2)


def examine(num):
    data = cache.get(num)
    if data == -1:
        result = num * num
        num = cache.set(num, result)

        print('Computing ......')
        time.sleep(3)
        return result
    else:
        return data


if __name__ == '__main__':
    begin = time.time()
    print(examine(11))
    print(examine(12))
    end = time.time()
    print('first examine of two iters:', end - begin)

    begin = time.time()
    print(examine(11))
    print(examine(12))
    print(examine(11))
    print(examine(12))
    end = time.time()
    print('second examine of double two iters:', end - begin)
