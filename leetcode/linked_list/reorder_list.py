class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return head
        (head, middle) = self.findMiddle(head)

        middle = self.reverseList(middle)
        return self.mergeList(head, middle)

    """
    split the middle. returns tuple with each halves
    reverse the second half of list
    merge them in place
    """
    def findMiddle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None

        return head, middle

    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    def mergeList(self, l1, l2):
        p1, p2 = l1, l2

        while p2:
            nextNode = p1.next
            p1.next = p2
            p1 = nextNode

            nextNode = p2.next
            p2.next = p1
            p2 = nextNode

        return l1


