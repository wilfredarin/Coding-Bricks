
test = int(input())
for i in range(test):
    n,m = map(int,input().split())
    dp = [[0]*m]*n
    dp[0] = [1]*m
    for i in range(n):
        dp[i][0]=1
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    print (dp[-1][-1]%(10**9+7))
