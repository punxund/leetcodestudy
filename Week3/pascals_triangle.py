# https://leetcode.com/problems/pascals-triangle/description/
# 2022-11-24

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # make n inner arrays with number 1
        pascal_triangle = [[1]]*numRows

        if numRows == 1:
            return pascal_triangle

        for i in range(1,numRows): # O(n^2)
            # every inner array has n number. first and last numbers are always 1.
            pascal_triangle[i]=[1]*(i+1)
            if i >= 2:
                # like the explaination, each number is the sum of the two numbers directly above it as shown.
                # update the number in the middle.         
                for j in range(1,i):
                    pascal_triangle[i][j] = pascal_triangle[i-1][j-1]+pascal_triangle[i-1][j]
        
        return pascal_triangle
            
        
