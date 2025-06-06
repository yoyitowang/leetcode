#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # TC: O(n)
        # SC: O(w) w is wide
        
        if not root:
            return 0
        
        dq = deque([root])
        dep = 0
        while dq:
            dep += 1
            for _ in range(len(dq)):
                node = dq.popleft()
                if not node.left and not node.right: return dep
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
        
        return dep

        # # -- recursive
        # # TC: O(n)
        # # SC: O(h)
        # if not root:
        #     return 0
        # if not root.left and root.right:
        #     return 1 + self.minDepth(root.right)
        # if not root.right and root.left:
        #     return 1 + self.minDepth(root.left)
        
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
             
# @lc code=end

