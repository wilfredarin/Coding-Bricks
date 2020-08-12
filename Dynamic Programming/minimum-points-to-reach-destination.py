#https://practice.geeksforgeeks.org/problems/minimum-points-to-reach-destination/0
#a = map(int,input().split())
#a = list(map(int,input().split()))

test = int(input())
for t in range(test):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    points = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            points[i][j] = a[i*m +j]
    dp = [[0 for i in range(m)] for i in range(n)]
    if points[-1][-1]>0:
        dp[-1][-1] = 1 
    else:
        dp[-1][-1] = abs(points[-1][-1])+1 
    #last col
    for i in range(n-2,-1,-1):
        dp[i][m-1] = max(1,dp[i+1][m-1]-points[i][m-1])
    #last row
    for i in range(m-2,-1,-1):
        dp[n-1][i] = max(1,dp[n-1][i+1]-points[n-1][i])
    
    #fill bottom up
    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            min_on_leave = min(dp[i+1][j],dp[i][j+1])
            dp[i][j] = max(1,min_on_leave-points[i][j])
    print(dp[0][0])
    
