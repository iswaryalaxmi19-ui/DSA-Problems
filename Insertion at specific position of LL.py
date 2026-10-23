def insertatspecificposition(head, x, pos):
    if head is None:
        return None
    new_node = Node(x)
    if pos == 0:
        new_node.next = head
        return new_node
    current = head
    for i in range(1,pos-1):
        if current is None:
            return head
        current = current.next
    if current is None:
        return head
    new_node.next= current.next
    current.next = new_node
    return head

