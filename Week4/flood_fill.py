# https://leetcode.com/problems/flood-fill/description/
# 2022-12-01 Hongsik Kim

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        first_color = image[sr][sc]

        # if first color is the filling color, then return directly image array.
        if color == first_color:
            return image

        # using dfs, we can fill color in the 4 directionally pixels.
        def Fill(x, y): # recursive so O(n), n is here the length of image array.                     
            if image[x][y] == first_color:
                image[x][y] = color
                if x-1 >= 0:
                    Fill(x-1, y)                              
                if y-1 >= 0:
                    Fill(x, y-1)         
                if x+1 < len(image):
                    Fill(x+1, y)
                if y+1 < len(image[0]):
                    Fill(x, y+1)                     
        
        Fill(sr, sc)

        return image  

            