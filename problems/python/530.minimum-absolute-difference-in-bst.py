#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        # inorder -> get order list
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        min_res = float('inf')
        for i in range(1, len(res)):
            min_res = min(res[i]-res[i-1], min_res)
        return min_res
    
        # # postorder
        # # TC: O(n)
        # # SC: O(h->n)
        # self.min_diff = float('inf')
        
        # def traversal(node):
        #     if not node:
        #         return float('inf'), float('-inf')
            
        #     # left > right > root
        #     # find largest val of left
        #     min_left, max_left = traversal(node.left)
        #     # find largest val of right
        #     min_right, max_right = traversal(node.right)
        #     # calculate and find the diff
        #     if max_left != float('-inf'):
        #         self.min_diff = min(self.min_diff, node.val - max_left)
        #     if min_right != float('inf'):
        #         self.min_diff = min(self.min_diff, min_right - node.val)

        #     return min(min_left, node.val), max(max_right, node.val)

        # traversal(root)
        # return self.min_diff
            
# @lc code=end

