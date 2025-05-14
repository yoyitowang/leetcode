#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
TreeNode.__lt__ = lambda a, b: a.val < b.val
TreeNode.__gt__ = lambda a, b: a.val > b.val

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if root < p and root < q:
            right = self.lowestCommonAncestor(root.right, p, q)
            if right:
                return right
        elif root > p and root > q:
            left = self.lowestCommonAncestor(root.left, p, q)
            if left:
                return left

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

