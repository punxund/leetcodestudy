#https://leetcode.com/problems/invert-binary-tree/description/
#2022-11-16 Hongsik Kim

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #if root is empty, return None
        if root is None: 
            return None

        #change left side and right side with recursive function
        x = self.invertTree(root.left) #O(n)?
        y = self.invertTree(root.right) #O(n)?
        root.right = x
        root.left = y
        
        #O(n)
        return root