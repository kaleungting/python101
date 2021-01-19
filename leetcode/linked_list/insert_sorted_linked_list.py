class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insert(self, head: 'Node', insertVal: int) -> 'Node':
    # if no head, then create a head and set it to itself

    if not head:
        head = Node(insertVal)
        head.next = head
        return head

    curr = head

    while True:
        currVal = curr.val
        nextVal = curr.next.val

        if currVal <= insertVal and insertVal <= nextVal:  # 2-8 insert 5
            break

        if currVal > nextVal:  # that means you've reached the pivot point
            if currVal <= insertVal and insertVal >= nextVal:  # 7-2  insert 8
                break
            elif currVal >= insertVal and insertVal <= nextVal:  # 7-2  insert 0
                break

        curr = curr.next

        if curr == head:  # if you've reached a full cycle and it hasn't hit anything yet
            break

    newNode = Node(insertVal)
    newNode.next = curr.next
    curr.next = newNode
    return head


# if curr val is less than value and curr.next val is greater than value, then we've come to the right place
# if that never happens, then it must be at the pivot point
# pivot point means, next number is less than curr
# if curr is less than curr.next, then you've reached a pivot point
    # if number is greater than curr, then curr.next = val
    # if number is less