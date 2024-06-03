class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        print(max_profit)
        return max_profit