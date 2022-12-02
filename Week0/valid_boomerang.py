# https://leetcode.com/problems/valid-boomerang/
# 2022-11-06 Hongsik Kim

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:   

        def is_same(a, b):
            return a[0] == b[0] and a[1] == b[1]

        a, b, c = points

        if is_same(a, b) or is_same(b, c) or is_same(c, a):
            return False

        if a[1]-points[1][1] == 0 or points[1][1]-points[2][1] == 0:
            return points[0][1]-points[1][1] != points[1][1]-points[2][1]
        
        return not math.isclose((points[0][0]-points[1][0])/(points[0][1]-points[1][1]), (points[1][0]-points[2][0])/(points[1][1]-points[2][1]))

        