
def lis(a,n):
	dp = [1]*n
	j =0
	i =1
	while i<n:
		while j<i:
			if a[j]<a[i]:
				dp[i]=max(dp[i],dp[j]+1)
			j+=1
		j=0
		i+=1
	return(max(dp))




test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    print(lis(a,n))
