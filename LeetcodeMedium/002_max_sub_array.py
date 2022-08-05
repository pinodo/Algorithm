# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
# sum and return its sum. A subarray is a contiguous part of an array.

# Example 1
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2
# Input: nums = [1]
# Output: 1

# Example 3
# Input: nums = [5,4,-1,7,8]
# Output: 23

# Constraints
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer
# approach, which is more subtle.


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if 1 <= len(nums) <= 10**5:
            # TRY_2
            # maxSum = 0
            # currentSum = nums[0]
            for i in nums:
                if -10**4 <= i <= 10**4:
                    # TRY_3
                    for i in range(1, len(nums)):
                        if nums[i - 1] > 0:
                            nums[i] += nums[i - 1]
                    return max(nums)

                    # TRY_2
                    # if currentSum < 0:
                    #     currentSum = 0
                    # currentSum += i
                    # if currentSum > maxSum:
                    #     maxSum = currentSum
                    # return max(maxSum, currentSum)
                else:
                    raise ValueError('Invalid value')
        else:
            raise ValueError('Invalid length')

        # TRY_1
        # total_prod = nums[0]
        # max_prod = 0
        # if len(nums) == 1:
        #     return nums[0]
        # else:
        #     for i in range(1, len(nums)):
        #         total_prod += nums[i]
        #         if nums[i] >= total_prod:
        #             total_prod = nums[i]
        #         # should implement when countering a negative value
        #         if nums[i] < 0:
        #             max_prod = total_prod - nums[i]
        # return max(total_prod, max_prod)


s = Solution()
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1]
nums3 = [5, 4, -1, 7, 8]
nums4 = [-2, -1]
print(s.maxSubArray(nums1))
print(s.maxSubArray(nums2))
print(s.maxSubArray(nums3))
print(s.maxSubArray(nums4))
