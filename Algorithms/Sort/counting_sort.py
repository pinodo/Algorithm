# Counting Sort: make a list that contains all range of data, then print from the start to the end
# Big O: O(N + K)
# Efficient if the range is short

arr = [7, 5, 9, 0, 2, 1, 5, 2, 6, 3, 8, 7, 0, 5, 2, 3]
# make a list that contains all range
count = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1  # increase the index of each elem value

for i in range(len(count)):  # check the recorded sort info to the list
    for j in range(count[i]):
        print(i, end=' ')
