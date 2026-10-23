def insertatbeginning(head, x):
     if head is None:
        return None
     new_node = Node(x)
     new_node.next = head
     head = new_node
     return head