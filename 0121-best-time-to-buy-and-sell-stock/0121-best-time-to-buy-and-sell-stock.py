class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        max_profit=0

        for i in prices:
            if i < lowest:
                lowest=i
            profit= i - lowest
            if profit > max_profit:
                max_profit= profit
        return max_profit

        