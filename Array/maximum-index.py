"""
Given an array A[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint of A[i] <= A[j].

Input:
The first line contains an integer T, depicting total number of test cases.  Then T test case follows. First line of each test case contains an integer N denoting the size of the array. Next line contains N space separated integeres denoting the elements of the array.

Output:
Print the maximum difference of the indexes i and j in a separtate line.

Constraints:
1 ≤ T ≤ 1000
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 1018

Example:
Input:
1
9
34 8 10 3 2 80 30 33 1

Output:
6

Explanation:
Testcase 1:  In the given array A[1] < A[7] satisfying the required condition(A[i] <= A[j]) thus giving the maximum difference of j - i which is 6(7-1).
"""



#a = map(int,input().split())
#a = list(map(int,input().split()))

def maxDistance(a):
    n = len(a)
    hash_table = {}
    for i in range(n):
        if a[i] in hash_table:
            hash_table[a[i]].append(i)
        else:
            hash_table[a[i]]=[i]
    index= n
    ans = 0
    a.sort()
    for i in range(n):
        if index>hash_table[a[i]][0]:
            index = hash_table[a[i]][0]
        
        ans = max(ans,hash_table[a[i]][-1]-index)
    return ans
test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    print(maxDistance(a))
        
    
    
