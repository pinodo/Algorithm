# The warrior ant is planning to attack the food storage.
# Given the number of storages and the number of each food amounts in each storage,
# Print the maximum food that the ant can deprive.

# Example 1
# Input
# 4
# 1 3 1 5
# Output
# 8


def max_food_nums(n, array):
    # Bottom-up
    storage_list = [0] * n
    storage_list[0] = array[0]
    storage_list[1] = max(array[0], array[1])
    for i in range(2, n):
        storage_list[i] = max(storage_list[i - 1], storage_list[i - 2] + array[i])
    return storage_list[n - 1]


storage_nums = int(input('Nums: '))
foods_count = list(map(int, input('Foods: ').split()))
print(max_food_nums(storage_nums, foods_count))
