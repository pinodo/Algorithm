# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
# range [1, n] that do not appear in nums.


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set([i for i in range(1, len(nums) + 1)]) - set(nums))


s = Solution()
l1 = [4, 3, 2, 7, 8, 2, 3, 1]
l2 = [1, 1]
print(s.findDisappearedNumbers(l1))
print(s.findDisappearedNumbers(l2))
