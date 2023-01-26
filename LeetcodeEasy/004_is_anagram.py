# Given two strings s ant t, return true if t is an anagram of s, and false otherwise
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            prev_s = ''.join(sorted(s))
            next_s = ''.join(sorted(t))
            return prev_s == next_s
        else:
            return False


sol = Solution()
s, t = input('s: '), input('t: ')
print(sol.isAnagram(s, t))