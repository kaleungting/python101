class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


"""
create a sentinel node to attach head to
set pointer = to dummy, this way you can ensure that the head is not the same as the val

while curr and curr.next    
    if curr.next.val is the same as val,
        rearrange the pointers
    else
        you continue to move along the linkedlist

return dummy.next

"""
