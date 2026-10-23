def insertatend(head,x):
    if head is None:
        return None

    new_node = Node(x)
    
    current = head

    while current is not None:
        current = current.next
    
    current.next = new_node

    return head