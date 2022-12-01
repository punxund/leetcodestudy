# https://leetcode.com/problems/valid-palindrome-ii/
# 2022-12-01 Hongsik Kim

class Solution:
    def validPalindrome(self, s: str) -> bool:

        #### time limit exceeded ####
        # str_array = list(s)      

        # def is_palindrome(arr):
        #     for i in range(len(arr)//2):     
        #         if arr[i] != arr[-(i+1)]:
        #             return False
        #     return True

        # for i in range(len(str_array)):
        #     x = str_array.pop(i)
        #     if is_palindrome(str_array):
        #         return True
        #     else:
        #         str_array.insert(i, x)
        return False