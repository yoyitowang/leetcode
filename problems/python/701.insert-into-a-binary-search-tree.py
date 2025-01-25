#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # recursive
        # # TC: O(h)
        # # SC: O(h)
        # if not root:
        #     return TreeNode(val)
        
        # # root > left > right
        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left, val)
        # elif root.val < val:
        #     root.right = self.insertIntoBST(root.right, val)

        # return root
    
        # iterative
        if not root:
            return TreeNode(val)
        
        cur = root
        while cur:
            # left
            if cur.val > val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            # right
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
        return root
             
# @lc code=end

