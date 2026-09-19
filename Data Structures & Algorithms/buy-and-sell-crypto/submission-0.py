class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        if len(prices) == 1:
            return 0

        l, r = 0, 1

        # l -> buy
        # r -> sell

        while r < len(prices):
            
            if prices[l] > prices[r]:

                l = r
                r += 1
            
            elif prices[l] <= prices[r]:
                cur_profit = prices[r] - prices[l]
                max_profit = max(max_profit, cur_profit)
                r += 1
        
        return max_profit
