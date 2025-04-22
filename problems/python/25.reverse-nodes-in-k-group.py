#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # TC: O(n)
        # SC: O(1)
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        
        dummy = ListNode(0, next=head)
        p0 = dummy
        while n >= k:
            n -= k
            prev = None
            cur = p0.next
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev, cur = cur, nxt
            p0_nxt = p0.next
            p0.next.next = cur
            p0.next = prev
            p0 = p0_nxt
        return dummy.next
                     
# @lc code=end

