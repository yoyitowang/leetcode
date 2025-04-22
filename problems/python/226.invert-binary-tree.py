#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        # TC: O(n)
        # SC: O(n)
        if not root:
            return None
        
        que = deque([root])
        while que:
            node = que.popleft()
            node.left, node.right = node.right, node.left

            if node.left: que.append(node.left)
            if node.right: que.append(node.right)
        
        return root

        # recursive
        # TC: O(n)
        # SC: O(h)
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
          
# @lc code=end

