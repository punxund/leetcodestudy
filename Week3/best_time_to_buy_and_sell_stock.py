# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 2022-11-25 Hongsik Kim

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # I tried but time limit exceeded
        # max_profit = 0        
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         if prices[j]-prices[i] > max_profit:
        #             max_profit = prices[j]-prices[i]                    
        # return max_profit
                    
        # max_profit_list = []            
        # for i in range(len(prices)-1):
        #     if prices[i] < max(prices[i+1:]):
        #         max_profit_list.append(max(prices[i:])-prices[i])
        # if max_profit_list == []:
        #     return 0
        # return max(max_profit_list)

