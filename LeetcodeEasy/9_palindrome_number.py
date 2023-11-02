# Given an integer x, return true if x is a palindrome, and false otherwise

# Ex 1
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Ex 2
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Ex 3
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = list(str(x))
        for i in range(len(num)//2):
            if num[i] != num[-i - 1]:
                return False
        return True


s = Solution()
print(s.isPalindrome(int(input('Enter the number: '))))
