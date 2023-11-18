# Given a string s, find the first non-repeating character in it
# and return its index. If it does not exist, return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] and s[i] not in s[i + 1:]:
                return i
        return -1


s = Solution()
print(s.firstUniqChar('leetcode'))  # return 0
print(s.firstUniqChar('loveleetcode'))  # return 2
print(s.firstUniqChar('aabb'))  # return -1
