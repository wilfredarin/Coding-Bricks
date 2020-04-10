#https://practice.geeksforgeeks.org/problems/subarray-with-0-sum/0
def checkSum(arr,n):
    if n==0:
        return "No"
    if n==1 and arr[0]!=0:
        return "No"
    sum = 0
    hash_map = {}
    for i in range(n):
        sum+=arr[i]
        if sum in hash_map or sum==0:
            return "Yes"
        else:
            hash_map[sum]=i
    return "No"
test = int(input())
for i in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    print(checkSum(arr,n))
