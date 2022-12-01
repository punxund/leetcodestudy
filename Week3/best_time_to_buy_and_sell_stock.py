# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 2022-11-25 Hongsik Kim

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # !!!!time limit exceeded!!!!
        # max_profit = 0        
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         if prices[j]-prices[i] > max_profit:
        #             max_profit = prices[j]-prices[i]                    
        # return max_profit
        return 0            
