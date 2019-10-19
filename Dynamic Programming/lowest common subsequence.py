def lcs(a1,a2,n1,n2):
    dp = [[0 for i in range(n1+1)] for j in range(n2+1)]
    
    for i in range(1,n2+1):
        for j in range(1,n1+1):
            if a2[i-1]!=a1[j-1]:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            else:
                dp[i][j]=dp[i-1][j-1]+1
    return dp[n2][n1]



test = int(input())
for i in range(test):
    n1,n2 = map(int,input().split())
    a1 = list(input())
    a2 = list(input())
    print(lcs(a1,a2,n1,n2))
