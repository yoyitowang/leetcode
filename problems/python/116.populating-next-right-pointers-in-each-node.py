#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # TC: O(n)
        # SC: O(n) != O(1)
        res = []
        if not root:
            return None
        from collections import deque
        dq = deque([root])
        while dq:
            prev = None
            for _ in range(len(dq)):
                node = dq.popleft()
                node.next = prev
                prev = node
                if node.right: dq.append(node.right)
                if node.left: dq.append(node.left)
        return root
# @lc code=end

