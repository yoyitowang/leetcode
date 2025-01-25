#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # TC: O(n)
        # SC: O(1) + O(h) stack of tree
        self.mode = []
        self.prev = None
        self.max = 0
        self.cnt = 0

        def dfs(node):
            if not node:
                return
            # left > root > right
            dfs(node.left)
            if self.prev == node.val:
                self.cnt += 1
            else:
                self.cnt = 0
            self.prev = node.val

            if self.cnt == self.max:
                self.mode.append(node.val)
            elif self.cnt > self.max:
                self.max = self.cnt
                self.mode = [node.val]
            dfs(node.right)
        dfs(root)

        return self.mode
            
# @lc code=end

