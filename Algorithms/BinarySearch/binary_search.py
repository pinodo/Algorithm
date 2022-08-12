# Binary Search: search the sorted array by lessen the range to the half
# set the range using start, mid, and end
# Big O: O(logN)
# Recursion

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # if found, return the index of the middle
    if arr[mid] == target:
        return mid
    # if the value is smaller than the middle value, find a left side
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    # if the value is bigger than the middle value, find a right side
    else:
        return binary_search(arr, target, mid + 1, end)


# n = number of elems, target = the value what we want to find
n, target = list(map(int, input().split()))

arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n - 1)
if result is None:
    print('Not found')
else:
    print(result + 1)