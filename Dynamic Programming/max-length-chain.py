#https://practice.geeksforgeeks.org/problems/max-length-chain/1
def maxChainLen(Parr, n):
    # Parr:  list of pair
    #code here
    A = []
    for i in Parr:
        A.append([i.a,i.b])
    A.sort()
    n = len(A)
    dp = [1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j][1]<A[i][0] and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
    return dp[-1]
