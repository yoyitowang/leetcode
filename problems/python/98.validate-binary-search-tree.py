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
        self.prev = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.treversal(root)
        
    def treversal(self, node):
        if not node:
            return True
        # left > root > right
        if not self.treversal(node.left):
            return False
        if self.prev != None and self.prev >= node.val:
            return False
        self.prev = node.val
        return self.treversal(node.right)
    
# @lc code=end

