#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # recursive
        # # TC: O(n)
        # # SC: O(h)
        # res = []

        # def dfs(node):
        #     if not node:
        #         return
            
        #     if node.left: dfs(node.left)
        #     res.append(node.val)
        #     if node.right: dfs(node.right)

        # dfs(root)
        # return res    

        #--
        # iterative
        # TC: O(n)
        # SC: O(n)
        res = []
        if not root:
            return res
        st = []
        cur = root
        while st or cur:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                cur = st.pop()
                res.append(cur.val)
                cur = cur.right
        return res
# @lc code=end

