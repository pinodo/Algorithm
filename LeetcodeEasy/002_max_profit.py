# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Ex1
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Ex2
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution:
    # Big O: O(n)
    def maxProfit(self, prices: list[int]) -> int:
        buy_index = 0
        sell_index = 1
        max_profit = 0
        if 1 <= len(prices) <= 10**5:
            while sell_index < len(prices):
                if 0 <= prices[buy_index] <= 10**4:
                    if prices[buy_index] < prices[sell_index]:
                        profit = prices[sell_index] - prices[buy_index]
                        max_profit = max(max_profit, profit)
                    else:
                        buy_index = sell_index
                    sell_index += 1
                else:
                    print('Invalid value')
        else:
            print('Invalid length')
        return max_profit


s = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
print(s.maxProfit(prices1))
print(s.maxProfit(prices2))
