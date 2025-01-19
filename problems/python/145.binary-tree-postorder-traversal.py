#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # recursive
        # # TC: O(n)
        # # SC: O(h)
        
        # res = []
        # def dfs(node):
        #     if not node:
        #         return
        #     if node.left: dfs(node.left)
        #     if node.right: dfs(node.right)
        #     res.append(node.val)

        # dfs(root)
        # return res

        # # --
        # # iterative
        # # TC: O(n)
        # # SC: O(n)/O(log n)
        # res = []
        # if not root:
        #     return res
        # st = [root]
        # # left > right > root
        # while st:
        #     node = st.pop()
        #     res.append(node.val)
        #     if node.left: st.append(node.left)
        #     if node.right: st.append(node.right)

        # return res[::-1]

        # --
        # iterative 2
        # TC: O(n)
        # SC: O(n)
        res = []
        if not root:
            return res
        st = [root]

        while st:
            node = st.pop()
            if node:
                # left > right > root
                st.append(node)
                st.append(None)
                if node.right: st.append(node.right)
                if node.left: st.append(node.left)
            else: # when it's None -> start append result
                node = st.pop()
                res.append(node.val)
        return res                
                
# @lc code=end

