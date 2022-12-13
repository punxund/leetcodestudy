# https://leetcode.com/problems/fair-candy-swap/
# 2022-12-08 Hongsik Kim

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        #### time limit exceededㅠㅠ ####
        # sum_alice = sum(aliceSizes)
        # sum_bob = sum (bobSizes)
        # answer=[0,0]
        # if sum_alice > sum_bob:
        #     x = (sum_alice-sum_bob)/2
        #     for i in aliceSizes:
        #         for j in bobSizes:
        #             if j+x == i:
        #                 answer[0] = i
        #                 answer[1] = j
        #                 return answer
        # else:
        #     y = (sum_bob-sum_alice)/2
        #     for i in aliceSizes:
        #         for j in bobSizes:
        #             if i+y == j:
        #                 answer[0] = i
        #                 answer[1] = j
                         return answer