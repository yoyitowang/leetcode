#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # TC: O(n)
        # SC: O(h)
        self.ans = 0
        if not root:
            return self.ans

        # 0: not covered
        # 1: camera
        # 2: covered
        def dfs(node):
            if not node:
                return 2
            
            # left > right > root
            left = dfs(node.left)
            right = dfs(node.right)

            # case 1:
            # 2/2
            if left == 2 and right == 2:
                return 0
            
            # case 2:
            # 0/0
            # 0/1, 1/0
            # 0/2, 2/0
            if left == 0 or right == 0:
                self.ans += 1
                return 1
            
            # case 3:
            # 1/1
            # 1/2, 2/1
            if left == 1 or right == 1:
                return 2

        if dfs(root) == 0: self.ans += 1
        
        return self.ans
# @lc code=end

