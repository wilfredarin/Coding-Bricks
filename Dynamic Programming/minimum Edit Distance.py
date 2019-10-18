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
    return d


def edit_distance(a1,a2,n1,n2):
	dp = [[-1 for i in range(n2+1)] for j in range(n1+1)]
	for i in range(n2+1):
		dp[0][i] =i
	for i in range(n1+1):
		dp[i][0]=i
	for i in range(1,n1+1):
		for j in range(1,n2+1):
			u = 0
			l = 0
			d = dp[i-1][j-1]
			if a1[i-1] == a2[j-1]:
				dp[i][j]=d
			elif a1[i-1] != a2[j-1]:
				u = dp[i-1][j]
				r = dp[i][j-1]
				dp[i][j]=min(d,u,r)+1
	return dp[n1][n2]
test = int(input())
for i in range(test):
    n1,n2 = map(int,(input().split(" ")))
    a1,a2 = input().split(" ")
    a1 =list(a1)
    a2 = list(a2)
    print(edit_distance(a1,a2,n1,n2))
