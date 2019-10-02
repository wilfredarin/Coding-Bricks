def deleteNode(curr_node):
    #code her
    temp = curr_node
    if not temp:
        return None
    while temp.next:
        p1 = temp.data
        p2 = temp.next.data
        temp.data = p2
        if not temp.next.next:
            temp.next =None
            return curr_node
        else:
            temp = temp.next
    return curr_node
        
