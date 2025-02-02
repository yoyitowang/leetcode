#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1
        cur = head
        mid = l//2
        for i in range(mid):
            cur = cur.next
        return cur       
# @lc code=end

