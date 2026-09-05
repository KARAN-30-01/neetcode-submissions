class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i=j=0
        min=float('inf')
        profit=0
        for a,b in enumerate(prices):
            if b<min:
                min =b
            profit = max(profit, b-min)

        return profit

        