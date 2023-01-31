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

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        repo = {}
        for i in range(len(nums)):
            elem = target - nums[i]
            if elem in repo:
                return [repo[elem], i]
            repo[nums[i]] = i


s = Solution()
nums1 = [2, 7, 11, 15]
target = 18
print(s.twoSum(nums1, target))