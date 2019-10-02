def segregate(head):
    #code here
    count = [0,0,0]
    temp = head 
    while temp:
        count[temp.data]+=1
        temp = temp.next
    count_0 = count[0]
    count_1 = count[1]
    count_2 = count[2]
    temp = head
    while count_0>0:
        temp.data = 0
        temp = temp.next
        count_0 -=1
    while count_1>0:
        temp.data = 1
        temp = temp.next
        count_1-=1
    while count_2>0:
        temp.data = 2
        temp = temp.next
        count_2 -=1
    return head
