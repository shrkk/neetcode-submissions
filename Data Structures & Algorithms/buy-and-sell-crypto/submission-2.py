class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need a buy and sell pointer
        buy = 0
        profit = 0
        for sell in range(len(prices)):
            # if the buy price is greaater than sell
            if prices[buy] > prices[sell]:
                buy = sell
            profit = max(profit, prices[sell] - prices[buy])
        
        return profit
            