#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        dummy = Node(0)
        prev = dummy
        while head:
            new = Node(
                x=head.val,
                random=head.random
            )
            hashmap[head] = new
            prev.next = new
            prev = new
            head = head.next
        
        cur = dummy
        while cur:
            if cur.random:
                cur.random = hashmap[cur.random]
            cur = cur.next
        return dummy.next
# @lc code=end

