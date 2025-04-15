#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__ = lambda a, b: a.val < b.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0: return None
        if n == 1: return lists[0]
        left = self.mergeKLists(lists[: n//2])
        right = self.mergeKLists(lists[n//2: ])
        return self.mergeTwoLists(left, right)
    
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode()
        while l1 and l2:
            if l1 < l2:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
# @lc code=end

