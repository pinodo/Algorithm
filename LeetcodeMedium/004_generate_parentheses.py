# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# Example 1:
# Input: n = 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
#
# Example 2:
# Input: n = 1
# Output: ["()"]
#
# Constraints:
# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def helper(left, right, val):
            if len(val) == n * 2:
                res.append(val)
                return
            if left < n:
                helper(left + 1, right, val + '(')
            if right < left:
                helper(left, right + 1, val + ')')
        res = []
        helper(0, 0, '')
        return res


s = Solution()
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))