#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # TC: O(n)
        # SC: O(n)
        res = []
        if not root:
            return res
        from collections import deque
        dq = deque([root])
        while dq:
            n = len(dq)
            tmp = []
            for i in range(n):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            res.append(tmp)
        return res[::-1]
              
# @lc code=end

