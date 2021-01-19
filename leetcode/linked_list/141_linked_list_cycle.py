def hasCycle(self, head: ListNode) -> bool:
    if head is None:
        return False
    slow, fast = head, head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next

    return True

"""
Set fast and slow pointer

if fast reaches the end, then no cycle
if fast equals to slow, then there's a cycle

"""