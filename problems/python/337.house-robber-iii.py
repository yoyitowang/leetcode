#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            
            # left > right > root
            left_y, left_n = dfs(node.left)
            right_y, right_n = dfs(node.right)
            # take root: left_n + right_n + root
            value_y = node.val + left_n + right_n
            value_n = max(left_y, left_n) + max(right_y, right_n)

            return value_y, value_n

        return max(dfs(root))      
# @lc code=end

