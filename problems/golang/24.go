/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func swapPairs(head *ListNode) *ListNode {
    dummy := &ListNode{Next: head}
    prev := dummy
    cur := head
    for cur != nil && cur.Next != nil {
        first := cur
        second := cur.Next
        third := cur.Next.Next

        prev.Next = second
        first.Next = third
        second.Next = first

        prev = first
        cur = third
    }

    return dummy.Next
}