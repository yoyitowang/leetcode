#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
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
        self.val = 0
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # TC: O(n)
        # SC: O(h)
        if not root:
            return None
        # right > root > left
        root.right = self.convertBST(root.right)
        self.val += root.val
        root.val = self.val
        root.left = self.convertBST(root.left)

        return root
         
# @lc code=end

