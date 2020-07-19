#Function should return an integer
#You may use python modules
#https://practice.geeksforgeeks.org/problems/sum-of-permutations/1
MOD = 10**9+7
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
def getSum(n, arr):
    #Code here
    sum_arr = sum(arr)
    fac = fact(n-1) #n!/n
    sum_tens = int(n*("1"))
    return (sum_arr*fac*sum_tens)%MOD
