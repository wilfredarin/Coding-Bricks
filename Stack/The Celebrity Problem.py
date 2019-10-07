def getId(m,n):
    s = []
    for i in range(n):
        s.append(i)
    A = s.pop()
    B = s.pop()
    while s:
        if knows(A , B):
            A = s.pop()
        else:
            B = s.pop()
    if knows(A,B):
        c= B
    else:
        c = A
    for i in range(n):
        if (i != c) and (knows(c,i) or (not knows(i,c))) :
            return -1
    return c
    
