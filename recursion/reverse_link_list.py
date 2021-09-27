def reverse_list(head):
    if head == None or head.next == None:
        return head
    p = reverse_list(head.next)
    head.next.next = head;
    head.next = None
    return p
