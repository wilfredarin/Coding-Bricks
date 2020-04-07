#https://practice.geeksforgeeks.org/problems/fractional-knapsack/0
#a = map(int,input().split())
#a = list(map(int,input().split()))


def kanpsack(val,wt,n,w):
	dp=  [[0 for i in range(w+1)] for i in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,w+1):
			if wt[i-1]>j:
				dp[i][j]=dp[i-1][j]
			else:
				dp[i][j]=max(dp[i-1][j-wt[i-1]]+val[i-1],dp[i-1][j])
	return dp[n][w]

test = int(input())
for i in range(test): 
    n = int(input())
    w = int(input())
    val = list(map(int,input().split()))
    wt = list(map(int,input().split()))
    print(kanpsack(val,wt,n,w))
    
    
    
