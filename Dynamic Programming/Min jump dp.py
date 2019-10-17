def str_list(a):
    k = len(a)
    d=""
    r = []
    for i in range(k):
        if a[i]!=" ":
            d+=a[i]
        else:
            r.append(int(d))
            d=""
        if i==k-1 and d:
            r.append(int(d))
    return r
    


def min_jump(a,n):
    if a[0]==0:
        return(-1)
    jumps = [-1 for i in range(n)]
    jumps[0] = 0
    for i in range(1,n):
        for j in range(i):
            if j+a[j]>=i and a[j]>0:
                jumps[i]=jumps[j]+1
                break
    return (jumps[-1])


test = int(input())
for i in range(test):
    
    n = int(input())
    a = list(input())
    a = str_list(a)
    print(min_jump(a,n))
    
