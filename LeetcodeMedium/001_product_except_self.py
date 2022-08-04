# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Follow up Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space
# for space complexity analysis.)


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zero_index = 0
        total_product = 1
        for i in nums:
            if i == 0:
                zero_index += 1
            else:
                total_product *= i
        result = []
        for i in nums:
            if zero_index == 0:
                result.append(total_product // i)
            else:
                # and: tests whether both expr are logically True
                # &: performs bitwise AND on the result of both statements
                if i == 0 and zero_index == 1:
                    result.append(total_product)
                else:
                    result.append(0)
        return result


s = Solution()
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]
nums3 = [0, 0]
nums4 = [0, 4, 0]
print(s.productExceptSelf(nums1))
print(s.productExceptSelf(nums2))
print(s.productExceptSelf(nums3))
print(s.productExceptSelf(nums4))
