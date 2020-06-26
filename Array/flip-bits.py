#https://practice.geeksforgeeks.org/problems/flip-bits/0
#a = map(int,input().split())
#a = list(map(int,input().split()))

def flipKadane(s):
    n = len(s)
    l = 0
    r = 0
    cur = 0
    max_diff = 0
    original_one = 0
    for i in range(n):
        if s[i]=="0":
            cur = max(1,cur+1)
        else:
            cur = max(-1,cur-1)
            original_one+=1
        max_diff = max(cur,max_diff)
    return max_diff+original_one
test = int(input())
for i in range(test):
    a = int(input())
    s = list(input().split())
    print(flipKadane(s))
