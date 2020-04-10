#https://practice.geeksforgeeks.org/problems/adjacents-are-not-allowed/0
def adjacent(n,arr):
    incl = max(arr[0][0],arr[1][0])
    excl = 0
    for i in range(1,n):
        temp  = incl
        now = max(arr[0][i],arr[1][i])
        incl = max(excl+now,incl)
        excl = temp
    return incl
    
test = int(input())
for i in range(test):
    n = int(input())
    c = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = []
    a.append(c)
    a.append(b)
    print(adjacent(n,a))
    
