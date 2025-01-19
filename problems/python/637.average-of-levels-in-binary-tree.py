#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root:
            return res

        from collections import deque
        dq = deque([root])
        while dq:
            _sum = 0
            for i in range((n:=len(dq))):
                node = dq.popleft()
                _sum += node.val
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            res.append(_sum/n)
        return res      
# @lc code=end

