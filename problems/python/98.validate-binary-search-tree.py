#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.vec = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.treversal(root)
        for i in range(1, len(self.vec)):
            if self.vec[i] <= self.vec[i-1]:
                return False
        
        return True
        
    def treversal(self, node):
        if not node:
            return 
        # left > root > right
        if node.left: self.treversal(node.left)
        self.vec.append(node.val)
        if node.right: self.treversal(node.right)
    
# @lc code=end

