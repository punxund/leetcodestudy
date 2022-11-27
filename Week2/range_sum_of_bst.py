#https://leetcode.com/problems/range-sum-of-bst/description/
#2022-11-17 Hongsik Kim

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int: 
        #make a node list of the range between low and higt
        list_dfs = []
        #search all nodes and append on the list if the node in the range
        def find_node(root) :
            if root is None:
                return None
            find_node(root.left) #O(n)
            find_node(root.right) #O(n)
            if root.val >= low and root.val <= high:
                list_dfs.append(root.val)
        #function start
        find_node(root)
        
        return sum(list_dfs) #O(n)
     
        
        
        