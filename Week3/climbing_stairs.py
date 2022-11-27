# https://leetcode.com/problems/climbing-stairs/description/
# 2022-11-25 Hongsik Kim

class Solution:
    def climbStairs(self, n: int) -> int:
        # first three number from example.
        ways_list = [1,2,3]        
        # the next number is like pibonacci the sum of the previous number and the number before.
        for i in range(3, n+1): # O(n)
            ways_list.append(ways_list[i-2]+ways_list[i-3])
        
        return ways_list[n-1] # O(n)