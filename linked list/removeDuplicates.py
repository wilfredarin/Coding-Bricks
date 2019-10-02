def removeDuplicates(head):
    #code here
    check = []
    temp = head
    prev = None

    while temp:
        
        if temp.data in check :
            T = temp.next
            prev.next = T
            temp = prev.next
           
            
        else:
            check.append(temp.data)
            prev = temp
            temp = temp.next
            
    return head
            
