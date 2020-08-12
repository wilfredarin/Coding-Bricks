#a = map(int,input().split())
#a = list(map(int,input().split()))
#https://practice.geeksforgeeks.org/problems/maximum-length-bitonic-subarray/0
test = int(input())
for t in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    inc = [1]
    prev = a[0]
    for i in range(1,n):
        if a[i]>prev:
            inc.append(inc[-1]+1)
        else:
            inc.append(1)
        prev = a[i]
    prev = a[-1]
    dec = [1]
    for i in range(n-2,-1,-1):
        if a[i]>prev:
            dec.append(dec[-1]+1)
        else:
            dec.append(1)
        prev = a[i]
    dec = dec[::-1]
    ans = 0
    for i in range(n):
        ans = max(ans,inc[i]+dec[i]-1)
    print(ans)
        
