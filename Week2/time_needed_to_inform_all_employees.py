#https://leetcode.com/problems/time-needed-to-inform-all-employees/
#2022-11-18 Hongsik Kim 

# This was not accepted in leedcode. Correct, but it tooks so long.
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        time_list = [0]*n
        time_list[headID] = 0        
        
        def time_update(n, manager, headID, informTime, time_list):
            for i in range(0, n): #O(n)
                if time_list[i] == 0 and i != headID:
                    if manager[i] == headID:
                        time_list[i] = time_list[headID] + informTime[headID]
                        time_update(n, manager, i, informTime, time_list) #O(n)

        time_update(n, manager, headID, informTime, time_list)

        return max(time_list)

        

