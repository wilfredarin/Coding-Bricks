#https://practice.geeksforgeeks.org/problems/word-break/0
def wordBreak(dic,arr,n):
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i]= 1 if arr[i] in dic else 0
    for l in range(1,n+1):
        for s in range(n-l):
            if arr[s:s+l+1] in dic:
                dp[s][s+l]=1
            else:
                for brk in range(s,s+l):
                    if dp[s][brk] and dp[brk+1][s+l]:
                        dp[s][s+l]=1
                        break
    return dp[0][-1]
        
        
    
test = int(input())
for i in range(test):
    q = int(input())
    dic = list(input().split())
    b = input()
    print(wordBreak(dic,b,len(b)))
        
        
