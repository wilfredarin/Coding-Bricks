def isPalindrome(head):
    #code here
    a = []
    temp =head
    while temp:
        a.append(temp.data)
        temp = temp.next
    l = len(a)
    if l<=1:
        return (1)
    copy = list(reversed(a[-(l//2):]))
    if copy == a[:l//2]:
        return 1
    else:
        return 0
