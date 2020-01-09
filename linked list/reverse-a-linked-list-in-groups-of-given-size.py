def reverse(head,k):
    current = head
    next = None
    prev = None
    count = 0
    while (current is not None and count<k):
        next = current.next
        current.next = prev
        #ChangeSituation
        prev = current
        current = next
        count+=1
    if current:
        head.next = reverse(next,k)
    return prev
