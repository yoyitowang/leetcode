#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # TC: O(n)
        # SC: O(h)
        self.ans = 0
        def dfs(node):
            height = 0
            if not node:
                return height
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left+right)
            
            return max(left, right) + 1
        
        dfs(root)
        return self.ans    
# @lc code=end

