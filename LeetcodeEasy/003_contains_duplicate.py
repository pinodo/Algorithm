# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if 1 <= len(nums) <= 10**5:
            index = 0
            if -10**9 <= nums[index] <= 10**9:
                if len(nums) == len(set(nums)):
                    return False
                else:
                    return True
                # TRY_1
                # sorted_nums = nums.copy()
                # sorted_nums.sort()
                # if sorted_nums[len(sorted_nums)-1] - sorted_nums[index] == len(sorted_nums) - sorted_nums[index] | len(sorted_nums) == 1:
                #     return False
                # else:
                #     return True
            else:
                raise ValueError('Invalid value')
        else:
            raise TypeError('Invalid length')


s = Solution()
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
nums4 = [1, 1]
print(s.containsDuplicate(nums1))
print(s.containsDuplicate(nums2))
print(s.containsDuplicate(nums3))
print(s.containsDuplicate(nums4))
