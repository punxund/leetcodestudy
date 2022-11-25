# https://leetcode.com/problems/reduce-array-size-to-the-half/description/
# 2022-11-25 Hongsik Kim

from itertools import combinations
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # make a dictionary with number counting
        dict_number = {}          
        for i in arr: # O(n)
            if i in dict_number:
                dict_number[i] += 1
            else:
                dict_number[i] = 1
        # sort by number counting
        new_dict = sorted(dict_number.items(), key=lambda x: x[1], reverse=True) # O(nlogn)
        
        # if sum_count is more than halb of array length, that's index+1 is what we are looking for.  
        sum_count = 0
        for number in new_dict:
            sum_count += number[1]
            if sum_count >= len(arr)/2:
                return new_dict.index(number)+1
        