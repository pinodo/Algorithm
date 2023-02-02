# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
#
# Example 1:
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        repo = {}
        for elem in strs:
            if ''.join(sorted(elem)) not in repo:
                repo[''.join(sorted(elem))] = [elem]
            else:
                repo[''.join(sorted(elem))].append(elem)
        res = []
        for i in repo:
            res.append(repo[i])
        return res


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))
