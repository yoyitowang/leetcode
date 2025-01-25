#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        # TC: O(n)
        # SC: O(h)
        def dfs(node, p, q):
            if not node:
                return
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)            
            if node.val == p.val or node.val == q.val:
                return node
                    
            if left and right:
                return node
            elif left:
                return left
            else:
                return right
        return dfs(root, p, q)     
# @lc code=end

