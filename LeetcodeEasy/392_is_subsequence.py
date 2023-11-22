# Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is
# a new string that is formed from the original string by deleting some (can be none) of the characters without
# disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec"
# is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        for c in range(len(t)):
            if len(s) == 0:
                break
            if s[0] is t[c]:
                s = s.replace(s[0], '', 1)
        return len(s) == 0


s = Solution()
print(s.isSubsequence('abc', 'ahbgdc'))  # return True
print(s.isSubsequence('axc', 'ahbgdc'))  # return False
