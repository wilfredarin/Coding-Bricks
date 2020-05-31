#stepping-numberswrong-output
#a = map(int,input().split())
#a = list(map(int,input().split()))

def dfs(n,m,i,count):
    if i>=n and i<=m:
        count[0]+=1
    if i==0 or i >m:
        return 
    lastD = i%10
    v1 = i*10+lastD-1
    v2 = i*10+lastD+1
    if lastD==0:
        dfs(n,m,v2,count)
    elif lastD==9:
        dfs(n,m,v1,count)
    else:
        dfs(n,m,v1,count)
        dfs(n,m,v2,count)
    
def stepNum(n,m):
    count = [0]
    for i  in range(10):
        dfs(n,m,i,count)
    return count[0]
test = int(input())
for i in range(test):
    n,m = map(int,input().split())
    print(stepNum(n,m))
