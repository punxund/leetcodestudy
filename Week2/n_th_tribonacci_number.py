#https://leetcode.com/problems/n-th-tribonacci-number/description/
#2022-11-17 Hongsik Kim

class Solution:
    def tribonacci(self, n: int) -> int:
        #I wanted to use recursive but it tooks long.- O(2^n)
        #return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        #So, using memoization
        #first make n memory
        d = [0]*n
        def tribo(n):
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            #if tribonacci number is there, then put out
            elif d[n-1] != 0:
                return d[n-1]
            #memo the tribo number on the list
            d[n-1] = tribo(n-1)+tribo(n-2)+tribo(n-3)
            return d[n-1] 
        return tribo(n) #O(n)

