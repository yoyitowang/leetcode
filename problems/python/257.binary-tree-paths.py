#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # TC: O(n)
        # SC: O(h)
        if not root:
            return []
        res = []
        def dfs(node, s):

            if s != "":
                s += "->" + str(node.val)
            else:
                s += str(node.val)

            # root
            if not node.left and not node.right:
                res.append(s)
                return
            # left
            if node.left: dfs(node.left, s)
            # right
            if node.right: dfs(node.right, s)

        dfs(root, "")
        return res

# @lc code=end

