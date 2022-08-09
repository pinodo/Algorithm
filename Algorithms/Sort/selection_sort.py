# Selection Sort: select the smallest data and change with the first order data, and repeat
# Big O: O(N^2)
# In python, sort library(sort()) is much faster than selection sort

arr = [7, 6, 4, 9, 0, 1, 5, 2, 8, 3]

for i in range(len(arr)):
    min_index = i  # index of the smallest elem
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]  # swapping

print(arr)
