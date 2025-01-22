#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # left
        left = self.sumOfLeftLeaves(root.left)
        # right
        right = self.sumOfLeftLeaves(root.right)
        # root
        mid = 0
        if root.left and not root.left.left and not root.left.right:
            mid = root.left.val
        res = mid + left + right
        return res     
# @lc code=end

