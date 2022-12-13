# https://leetcode.com/problems/group-anagrams/description/
# 2022-12-09 Hongsik Kim

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make dictionary to make group for anagram.
        anagram_dict = {}
        for str in strs: # O(nmlogn) i guess, n is here length of strs. 
            # first we have to know how each str is structured
            sorted_str_list = sorted(str) # O(nlogn) 
            sorted_str = ''.join(sorted_str_list)
            # if str has same structure, save on the dictionary in the anagram group
            if sorted_str in anagram_dict.keys(): # O(m), m is length of anagram groups.
                anagram_dict[sorted_str].append(str)
            else: 
                anagram_dict[sorted_str] = [str]
        
        return anagram_dict.values()

