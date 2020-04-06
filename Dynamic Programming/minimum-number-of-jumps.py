#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0
def minJump2(a,n):
    if n==0 or a[0]==0:
        return -1
    jumps = [float("inf") for i in range(n)]
    jumps[0] = 0
    for cur in range(1,n):
        for prev in range(cur):
            if cur <= prev + a[prev] and jumps!=float("inf"):
                jumps[cur]=min(jumps[cur],jumps[prev]+1)
                break   
    if jumps[-1]==float("inf"):
        return -1
    else:
        return jumps[-1]
test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    print(minJump2(a,n))
