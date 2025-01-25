#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # TC: O(n+m)
        # SC: O(n)
        self.res = defaultdict(int)

        def dfs(node):
            if not node:
                return
            # left > root > right
            dfs(node.left)
            self.res[node.val] += 1
            dfs(node.right)
        dfs(root)

        mode = []
        cur_max = 0
        for k, v in self.res.items():
            if v > cur_max:
                mode = [k]
                cur_max = v
            elif v == cur_max:
                mode.append(k)
        return mode
            
# @lc code=end

