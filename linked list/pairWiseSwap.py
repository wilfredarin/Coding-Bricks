def pairWiseSwap(head):
    #code_here
    temp = head
    while temp.next:
        p1 = temp.data
        p2 = temp.next.data
        temp.data = p2
        temp.next.data =p1
        if not temp.next.next:
            temp = temp.next
        else:
            temp = temp.next.next
    return head
