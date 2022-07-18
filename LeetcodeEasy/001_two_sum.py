# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Ex1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

# Ex2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

def two_sum(nums: list[int], target: int) -> list[int]:
    # Big O: (n^2)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i, j]
    return nums


def main():
    list1 = [2, 7, 11, 15]
    list2 = [3, 2, 4]
    list3 = [3, 3]

    target1 = 9
    target2 = 6
    target3 = 6

    print(two_sum(list1, target1))
    print(two_sum(list2, target2))
    print(two_sum(list3, target3))


if __name__ == "__main__":
    main()
