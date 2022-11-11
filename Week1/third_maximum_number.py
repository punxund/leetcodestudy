#https://leetcode.com/problems/third-maximum-number/
#2022-11-11 Hongsik Kim

#from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #eliminate the same value(redundant)
        data = set(nums)
        #sort the list in descending order 
        maximum_order = list(data)
        maximum_order.sort(reverse=True)
        #If the third maximum does not exist, return the maximum number.
        if len(maximum_order) >= 3 :
            return maximum_order[2]
        else :
            return maximum_order[0]
        