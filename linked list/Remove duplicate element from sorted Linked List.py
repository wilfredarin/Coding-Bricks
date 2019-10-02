def removeDuplicates(head):
    #code here
    temp = head
    while temp.next:
        if temp.data == temp.next.data:
            T = temp.next.next
        
            temp.next = T
        else:
            temp = temp.next
    return head
