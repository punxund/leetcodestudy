# https://leetcode.com/problems/binary-search/description/
# 2022-12-08 Hongsik Kim

from bisect import bisect_right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # using bisect find index of target if there is not, return -1
        return bisect_right(nums, target)-1 if nums[bisect_right(nums, target)-1] == target else -1