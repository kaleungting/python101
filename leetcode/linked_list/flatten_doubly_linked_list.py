def flatten(head):
    if not head:
        return None

    dummy = Node(0, None, None, None)
    prev = dummy
    stack = [head]

    while len(stack):
        curr = stack.pop()
        curr.prev = prev
        prev.next = curr

        if curr.next:
            stack.append(curr.next)

        if curr.child:
            stack.append(curr.child)
            curr.child = None

        prev = curr

    dummy.next.prev = None
    return dummy.next

