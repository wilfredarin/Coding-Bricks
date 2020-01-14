def spiralOrder(A):
        n = len(A)
        m = len(A[0])
        r = 0
        c = 0
        b = []
        if m ==n ==1:
            print(A[0][0])
            return
        while r<n and c<m:
            for i in range(c,m):
                b.append(A[r][i])
            r+=1 
            for j in range(r,n):
                b.append(A[j][m-1])
            m -=1 
            
            if r<n:
                for i in range(m-1,c-1,-1):
                    b.append(A[n-1][i])
                n-=1 
            if c<m:
                for j in range(n-1,r-1,-1):
                    b.append(A[j][c])
                c+=1 
        print(*b)
test = int(input())
for i in range(test):
    n,m =map(int,input().split())
    b = list(map(int,input().split()))
    A = [[0 for i in range(m)] for j in range(n)]
    k = -1
    for i in range(n*m):
        j =i%m
        if j==0:
            k+=1
        A[k][j] =b[i]
    spiralOrder(A)
