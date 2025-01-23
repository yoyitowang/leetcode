#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # root
        if not root.left and not root.right:
            if targetSum == root.val:
                return True
            else:
                return False
        # left
        left = self.hasPathSum(root.left, targetSum-root.val)
        # right
        right = self.hasPathSum(root.right, targetSum-root.val)
        
        return left or right
       
# @lc code=end

