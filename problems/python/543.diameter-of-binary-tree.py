#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # TC: O(n)
        # SC: O(h)
        ans = [0]        
        def dfs(node, h):
            if not node:
                return 0
            # calculate the height by postorder
            # left > right > root
            left = dfs(node.left, h)
            right = dfs(node.right, h)
            h[0] = max(h[0], left+right)

            return max(left, right) + 1

        _ = dfs(root, ans)
        return ans[0]    
# @lc code=end

