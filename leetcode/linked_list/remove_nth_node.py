class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # we want to initialize a dummy node, so we can start the left pointer at one ahead, so we can remove the node
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next
