def reverse_help(head):
    prev = None
    current  = head
    next = None
    while current:
        next = current.next
        current.next = prev
        #ChangeSituation
        prev = current
        current = next
    return prev

def compute(head):
    head = reverse_help(head)
    current = head
    max = head
    prev = None
    next = current.next 
    while current:
        
        next = current.next
        if max.data > current.data :
            prev.next = next
            current = next
            
        else:
            max = current
            prev = current
            current = next
            
    head = reverse_help(head)
