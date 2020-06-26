#https://practice.geeksforgeeks.org/problems/overlapping-intervals/0
#a = map(int,input().split())
#a = list(map(int,input().split()))

test = int(input())
for i in range(test):
    n = int(input())
    l = list(map(int,input().split()))
    j = 0
    A = []
    while j <2*n:
        A.append([l[j],l[j+1]])
        j+=2
    A.sort()
    stack =  [A[0]]
    for i in range(1,n):
        
        pre = stack.pop()
        a = pre[0]
        b = pre[1]
        
        cur = A[i]
        c  = cur[0]
        d = cur[1]
        
        
        if a<=c and c<=b:
            if d<=b:
                stack.append([a,b])
            else:
                stack.append([a,d])
        
        else:
            stack.append(pre)
            stack.append(cur)

    ans = []
    for i in stack:
        print(str(i[0]),end=" ")
        print(str(i[1]),end=" ")
    print()
    
        
