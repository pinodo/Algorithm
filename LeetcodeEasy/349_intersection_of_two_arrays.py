# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
# unique and you may return the result in any order.


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        min_lst, max_lst, res = min(nums1, nums2), max(nums1, nums2), []
        for i in min_lst:
            if i in max_lst:
                res.append(i)
        return set(res)


s = Solution()
print(s.intersection([1, 2, 2, 1], [2, 2]))
print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
