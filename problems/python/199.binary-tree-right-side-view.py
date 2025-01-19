#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        from collections import deque
        dq = deque([root])
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if i == 0:
                    res.append(node.val)
                if node.right: dq.append(node.right)
                if node.left: dq.append(node.left)
        return res
              
# @lc code=end

