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
def coin_change(coins,n_coins,total):	
	dp = [[-1 for i in range(total+1)] for j in range(n_coins+1)]
	for i in range(total+1):
		dp[0][i]=0
	dp[0][0] = 1
	for j in range(n_coins+1):
		dp[j][0] = 1
	for i in range(1,n_coins+1):
		for j in range(1,total+1):
			new_coin = coins[i-1]
			if new_coin>j:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = dp[i][j-new_coin]+dp[i-1][j]
	return dp[n_coins][total]
test = int(input())
for i in range(test):
    n_coins = int(input())
    g = list(input())
    total = int(input())
    coins = str_list(g)
    print(coin_change(coins,n_coins,total))
    
    
    
