class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = float('inf')
        res = float('-inf')

        for p in prices:

            buy = min(buy, p)
            res = max(res, p - buy)
        
        return res