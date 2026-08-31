class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum = float('inf')

        for p in prices:
            if p < minimum:
                minimum = p
                continue
                
            profit = p - minimum
            if profit > max_profit:
                max_profit = profit

        return max_profit