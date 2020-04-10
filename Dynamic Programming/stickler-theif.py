#https://practice.geeksforgeeks.org/problems/stickler-theif/0
def NonContSum(n,arr):
    if n==0:
        return 0
    incl = arr[0]
    excl = 0
    for i in range(1,n):
        temp = incl
        incl = max(incl,excl+arr[i])
        excl = temp
    return incl
        
        
test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    print(NonContSum(n,a))
