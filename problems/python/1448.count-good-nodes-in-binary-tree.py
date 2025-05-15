#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        res = [0]
        cur_max = float('-inf')
        def dfs(node, cmax):
            if not node:
                return
            if node.val >= cmax:
                res[0] += 1
            cmax = max(node.val, cmax)
            dfs(node.left, cmax)
            dfs(node.right, cmax)

        dfs(root, cur_max)

        return res[0]
# @lc code=end

