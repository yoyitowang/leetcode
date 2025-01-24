#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # preorder: root > left > right
        # inorder:  left > root > right

        root_val = preorder[0]
        root = TreeNode(root_val)

        # find the split index
        idx = inorder.index(root_val)

        # inorder split by idx
        inorder_left = inorder[: idx]
        inorder_right = inorder[idx+1: ]

        # preorder split by idx
        preorder_left = preorder[1: 1+len(inorder_left)]
        preorder_right = preorder[-len(inorder_right): ]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root   
# @lc code=end

