
#count-ways-to-reach-the-nth-stair/
#https://practice.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair/0/
arr=[0]*(100002)
arr[0]=1
for j in range(1,100001):
        arr[j]=((arr[j-2])+(arr[j-1]))%1000000007
test = int(input())
for i in range(test):
    n = int(input())
    print(arr[n])
