#length-unsorted-subarray

def unsortedArray(A):
    l = len(A)
    cur = A[0]
    s = -1
    e = -1
    for i in range(1,l):
        Next = A[i]
        if Next<cur:
            s = i-1
            break
        cur = A[i]
    cur = A[-1]
    for i in range(l-2,-1,-1):
        Next = A[i]
        if Next>cur:
            e = i+1
            break
        cur = A[i]
    # print(A[s:e+1])
    if s== -1 and e ==-1:
        return (0,0)
    
    else:
        mi = min(A[s:e+1])
        ma = max(A[s:e+1])
    for i in range(s):
        if A[i]>mi:
            s = i
            break
    for i in range(l-1,e,-1):
        if A[i]<ma:
            e = i
            break
    return (s,e)
    
        
        
        
