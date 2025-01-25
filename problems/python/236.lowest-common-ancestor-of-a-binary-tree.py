#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # TC: O(n)
        # SC: O(h)
        if not root:
            return
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)            
        if root.val == p.val or root.val == q.val:
            return root
                
        if left and right:
            return root

        return left or right  
# @lc code=end

