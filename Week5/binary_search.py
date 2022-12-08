# https://leetcode.com/problems/binary-search/description/
# 2022-12-08 Hongsik Kim

from bisect import bisect_right

class Solution:
    def search(nums: list[int], target: int) -> int:
        # using bisect find index of target if there is not, return -1
        #return bisect_right(nums, target)-1 if nums[bisect_right(nums, target)-1] == target else -1

        # without bisect
        start, end = 0, len(nums)-1
        mid, mid2 = int, int
        while mid2!=mid:
            mid = int((start+end)/2)
            print(mid)
            if target == nums[mid]:
                return mid
            else:
                mid2 = mid
                if nums[mid] > target:
                    end = end/2
                elif nums[mid] < target:
                    start = mid
        return -1
    
    print(search([-1,0,3,5,9,12], 3))