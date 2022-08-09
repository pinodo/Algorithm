# Quick Sort: Set the standard data(pivot), and swap the smaller and bigger ones
# Big O: Regular - O(NlogN), Worst: O(N^2)

arr = [7, 6, 4, 9, 0, 1, 5, 2, 8, 3]


def quick_sort(arr, start, end):
    if start >= end:  # end if num of elem is 1
        return
    pivot = start  # pivot = first elem
    left = start + 1
    right = end
    while left <= right:
        # repeat until find the bigger data than pivot
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # repeat until find the smaller data than pivot
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            # if crossed, change the smaller data and pivot
            arr[right], arr[pivot] = arr[pivot], arr[right]
            # if not crossed, change the smaller data and the bigger data
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # after the division, execute the quick sort both in the left and right side
    # Recursion
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


def quick_sort_comprehension(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_comprehension(left_side) + [pivot] + quick_sort_comprehension(right_side)


quick_sort(arr, 0, len(arr) - 1)
print(arr)
arr = [7, 6, 4, 9, 0, 1, 5, 2, 8, 3]
print(quick_sort_comprehension(arr))