#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        from collections import deque
        dq = deque([root])
        while dq:
            tmp = float('-inf')
            for i in range((n:=len(dq))):
                node = dq.popleft()
                tmp = max(tmp, node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            res.append(tmp)
        return res    
# @lc code=end

