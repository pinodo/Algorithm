# merge sort: divide the array, arrange, and merge
# limitation: inefficient memory usage: additional u, v
# Big O: log(2n)

def merge_sort(s):
    n = len(s)
    if n <= 1:
        return s
    else:
        mid = n // 2
        u = merge_sort(s[0: mid])
        v = merge_sort(s[mid: n])
        return merge(u, v)


def merge(u, v):
    s = []
    i = j = 0
    while i < len(u) and j < len(v):
        if u[i] < v[j]:
            s.append(u[i])
            i += 1
        else:
            s.append(v[j])
            j += 1
    if i < len(u):
        s += u[i: len(u)]
    else:
        s += v[j: len(v)]
    return s


arr = [5, 1, 3, 8, 7, 2]
result = merge_sort(arr)
print(result)
