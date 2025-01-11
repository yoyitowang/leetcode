#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # TC: O(n) n is the node number of linked list
        # SC: O(1)
        
        dummy = slow = fast = ListNode(next=head)
        for _ in range(n+1):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
            
        slow.next = slow.next.next if slow.next else None        
        
        return dummy.next
        
# @lc code=end

