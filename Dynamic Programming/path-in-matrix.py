#https://practice.geeksforgeeks.org/problems/path-in-matrix/0
test = int(input())
for t in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    m = n
    dp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j] = a[i*m +j]
    for i in range(1,n):
        for j in range(m):
            if j==n-1:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+dp[i][j]
            elif j==0:
                dp[i][j] = max(dp[i-1][j+1],dp[i-1][j])+dp[i][j]
            else:
                dp[i][j] = max(dp[i-1][j+1],dp[i-1][j],dp[i-1][j-1])+dp[i][j]
    print(max(dp[-1]))
    
    
