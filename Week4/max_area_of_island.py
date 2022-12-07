# https://leetcode.com/problems/max-area-of-island/submissions/853333645/
# 2022-12-02 Hongsik Kim

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # declare the maximum length
        m, n = len(grid), len(grid[0])

        # using dfs, we count the area of island. 
        def dfs(i,j):
            global area_counter
            area_counter += 1
            # we change the number, so let us know what we checked already.
            grid[i][j] = 2
            # 4 directionally recursion
            if i-1 >= 0 and grid[i-1][j] == 1:
                dfs(i-1, j)
            if j-1 >= 0 and grid[i][j-1] == 1:
                dfs(i, j-1)
            if i+1 <= m-1 and grid[i+1][j] == 1:
                dfs(i+1, j)
            if j+1 <= n-1 and grid[i][j+1] == 1:
                dfs(i, j+1)         
        
        max_area = 0
        global area_counter
        for i in range(m): # time complexity : O(n), n is here the length of grid matrix.
            for j in range(n):
                # if the number is 1(land), use dfs.
                if grid[i][j] == 1:
                    area_counter = 0
                    dfs(i, j) 
                    # update, if the area is more than max_area.
                    if max_area < area_counter:
                        max_area = area_counter
                                           
        return max_area