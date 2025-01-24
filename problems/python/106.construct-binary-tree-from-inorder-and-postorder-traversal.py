#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        # inorder:   left > root > right
        # postorder: left > right > root

        root_val = postorder[-1]
        root = TreeNode(root_val)
        # the root index of inorder
        idx = inorder.index(root_val)
        
        # inorder: split by index
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]

        # postorder : split by index
        postorder_left = postorder[: len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder)-1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root

# @lc code=end

