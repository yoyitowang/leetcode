#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, cur = dummy, head
        while cur and cur.next:
            first = cur
            second = cur.next
            third = cur.next.next

            prev.next = second
            second.next = first
            first.next = third

            prev = first
            cur = third

        return dummy.next       
        
# @lc code=end

