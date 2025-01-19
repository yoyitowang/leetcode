#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # TC: O(n)
        # SC: O(n)
        res = []
        if not root:
            return res
        from collections import deque
        dq = deque([root])
        while dq:
            tmp = []
            for i in range((n:=len(dq))):
                node = dq.popleft()
                tmp.append(node.val)
                if node.children: dq.extend(node.children)
            res.append(tmp)
        
        return res     
# @lc code=end

