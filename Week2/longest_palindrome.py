# https://leetcode.com/problems/longest-palindrome/description/
# 2022-11-18 Hongsik Kim

class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        alpha_list = list(s)
        alpha_set = set(alpha_list)
        count_list = []
        is_odd_number = False
        
        # Count number of the each alphabet
        for i in alpha_set: # O(n)
            count_list.append(alpha_list.count(i)) # O(n)

        # If the number of alphabets is even, the length is added by that number. 
        for j in count_list: # O(n)
            if j % 2 == 0:
                length += j
        # If the number of alphabets is even, the length is added by that number-1.
            else:
                length += j-1
                is_odd_number = True
        
        #At the end, add one alphabet in the middle.
        if is_odd_number:
            length += 1

        return length # O(n^2)        