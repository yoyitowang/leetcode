#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val > q.val and root.val > p.val:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = None
        elif root.val < q.val and root.val < p.val:
            left = None
            right = self.lowestCommonAncestor(root.right, p, q)
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        
        if root.val == p.val or root.val == q.val:
            return root
        
        return left or right  
# @lc code=end

