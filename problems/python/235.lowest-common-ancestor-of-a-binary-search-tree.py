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
            if left:
                return left
        elif root.val < q.val and root.val < p.val:
            right = self.lowestCommonAncestor(root.right, p, q)
            if right:
                return right
        return root
    
        # # iterative
        # # TC: O(h)
        # # SC: O(1)
        # while root:
        #     if root.val < p.val and root.val < q.val:
        #         root = root.right
        #     elif root.val > p.val and root.val > q.val:
        #         root = root.left
        #     else:
        #         break

        # return root
        
# @lc code=end

