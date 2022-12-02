# https://leetcode.com/problems/rotate-image/description/
# 2022-12-02 Hongsik Kim

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        j = 0
        # rotate the outermost numbers    
        # for i in range(n):
        #     print(i, n)
        #     x = matrix[0][i]
        #     matrix[0][i] = matrix[n-i][0]
        #     matrix[n-i][0] = matrix[n][n-i]
        #     matrix[n][n-i] = matrix[i][n]
        #     matrix[i][n] = x

        # first rotate the outermost numbers 90 degree and repeat numbers inside square.
        while n >= 1 and j <= n: # time complexity : O(n), n is here the length of all numbers(matrix). 
            for i in range(j, n):
                #print(i, j, n)
                x = matrix[j][i]
                matrix[j][i] = matrix[n-i+j][j]
                matrix[n-i+j][j] = matrix[n][n-i+j]
                matrix[n][n-i+j] = matrix[i][n]
                matrix[i][n] = x
            n -= 1
            j += 1