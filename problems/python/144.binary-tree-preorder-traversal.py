#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # recursive
        # # TC: O(n)
        # # SC: O(h) h is height of tree
        # res = []
        
        # def dfs(node):
        #     if not node:
        #         return
            
        #     res.append(node.val)
        #     if node.left: dfs(node.left)
        #     if node.right: dfs(node.right)
        
        # dfs(root)
        # return res

        # --
        # iterative
        # TC: O(n)
        # SC: O(h)
        res = []
        if not root: return res
        st = [root]
        while st:
            node = st.pop()
            if node:
                if node.right: st.append(node.right)
                if node.left: st.append(node.left)
                st.append(node)
                st.append(None)
            else:
                node = st.pop()
                res.append(node.val)
        
        return res
# @lc code=end

