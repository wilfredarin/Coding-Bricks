#https://practice.geeksforgeeks.org/problems/zero-sum-subarrays/0
def zeroSubArr(n,arr):
    hash_map ={0:[-1]}
    sum = 0
    ans = 0
    for i in range(n):
        sum+=arr[i]
        if sum in hash_map:
            hash_map[sum].append(i)
        else:
            hash_map[sum]=[i]
    for i in hash_map:
        t = hash_map[i]
        t = len(t)-1
        #subsets possible for n things
        ans += (t*(t+1))//2
    return ans
test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    print(zeroSubArr(n,a))
