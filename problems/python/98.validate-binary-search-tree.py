#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, min_v, max_v):
            if not node:
                return True
            if not min_v < node.val < max_v:
                return False
            left = dfs(node.left, min_v, node.val)
            right = dfs(node.right, node.val, max_v)
            
            return left and right
        
        return dfs(root, float('-inf'), float('inf'))
                  
# @lc code=end

