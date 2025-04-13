#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        # reverse the second nodes
        while second:
            tmp = second.next
            second.next = prev
            prev, second = second, tmp

        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next, second.next = second, t1
            first, second = t1, t2
# @lc code=end

