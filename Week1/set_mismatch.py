#https://leetcode.com/problems/set-mismatch/
#2022-11-11 Hongsik Kim

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #Find the number that occurs twice
        #duplicated_num = [i for i in nums if nums.count(i) == 2][0]
        #the missing_num is a number from 1 to n that is not in array nums
        #missing_num = [j for j in range(1,len(nums)+1) if j not in nums]
        #answer = [duplicated_num] + missing_num
        
        
        missing_num = []
        
        for i in range(1,len(nums)+1) : 
            if i not in nums :
                missing_num.append(j)               
            else :
                nums.remove(j)
        
        answer = nums + missing_num
        return answer