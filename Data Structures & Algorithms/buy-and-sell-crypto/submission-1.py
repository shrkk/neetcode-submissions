class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        profits = []
        for x in range(len(prices)-1):
            if prices[x] >= max(prices[x+1:]):
                profits.append(0)
            else:
                profits.append(
                    max(prices[x+1:]) - prices[x]
                )
        return max(profits)
