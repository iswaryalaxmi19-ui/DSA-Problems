def deletionatspecificposition(head, position):
    if head is None:
        return None
    if position == 0:
        return head.next
    current = head
    for i in range(1, position):
        if current is None:
            return head
        current = current.next
    if current is None or current.next is None:
        return head
    current.next = current.next.next
    return head