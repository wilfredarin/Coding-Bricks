def check(a,n,su):
    dp = [[0 for i in range(su+1)] for j in range(n+1)]
    
    for i in range(n+1):
        dp[i][0]=True
    for j in range(1,su+1):
        dp[0][j] = False
    for val in range(1,n+1):
        for s in range(1,su+1):
            if a[val-1]>s :
                dp[val][s] = dp[val-1][s]
            else:
                dp[val][s] = dp[val-1][s] or dp[val-1][s-a[val-1]] 
    
    return dp[n][su]
    
    
for i in range(int(input())):
    n = int(input())
    g = list(input())
    d=""
    a = []
    for i in range(len(g)):
        if g[i]!=" ":
            d+=g[i]
        else:
            a.append(int(d))
            d=""
        if i==len(g)-1 and d:
            a.append(int(d))
    su = sum(a)
    if su%2!=0:
        print("NO")
    else:
        su = su//2
        if check(a,n,su):
            print("YES")
        else:
            print("NO")
