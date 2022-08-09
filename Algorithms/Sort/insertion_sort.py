# Insertion Sort: insert the unprocessed elem to a proper index
# Big O: O(N^2), best: O(N) - if the array is already sorted

arr = [7, 6, 4, 9, 0, 1, 5, 2, 8, 3]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):  # from index i to 1, decreasing 1
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:  # if counter the smaller elem than self, stop
            break

print(arr)
