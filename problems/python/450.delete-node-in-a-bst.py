#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # TC: O(h)/O(log n)
        # SC: O(h)
        if not root:
            return None

        if root.val == key:
            # None
            if root.left == root.right:
                return None
            # no right
            elif root.right is None:
                return root.left
            # no left
            elif root.left is None:
                return root.right
            # left and right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root
# @lc code=end

