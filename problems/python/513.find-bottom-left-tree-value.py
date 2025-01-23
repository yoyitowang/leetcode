#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return None
        que = deque([root])
        while que:
            res = None
            for i in range(len(que)):
                node = que.popleft()
                if i == 0:
                    res = node.val
                if node.left: que.append(node.left)
                if node.right:que.append(node.right)
        return res
    
    # def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    #     self.res = None
    #     self.max_dep = float('-inf')
    #     self.dfs(root, 0)

    #     return self.res

    # def dfs(self, node, dep):
    #     if not node:
    #         return
    #     if not node.left and not node.right:
    #         if dep > self.max_dep:
    #             self.max_dep = dep
    #             self.res = node.val
    #     self.dfs(node.left, dep+1)
    #     self.dfs(node.right, dep+1)
# @lc code=end

