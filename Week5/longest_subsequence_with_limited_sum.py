# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
# 2022-12-08 Hongsik Kim

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # sort the numbers in ascending order
        nums.sort() # O(nlogn)

        answer = []
        for query in queries: # O(nm), n is length of nums and m is length of quries.
            sum_of_nums = 0
            count = 0
            # add number in nums array one by one 
            for num in nums:
                sum_of_nums += num
                # if sum of numbers less than or equal to query then count up
                if sum_of_nums <= query:                  
                    count += 1
                else:
                    break
            answer.append(count)
        
        return answer # time complexity : O(nm+nlogn) 
            
        