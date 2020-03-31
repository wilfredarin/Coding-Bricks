"""
Given a string S, find the longest palindromic substring in S. 
Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S).
Palindrome string: A string which reads the same backwards.
More formally, 
S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first 
( with the least starting index ).

NOTE: Required Time Complexity O(n2).

Input:
The first line of input consists number of the testcases. The following T lines consist of a string each.

Output:
In each separate line print the longest palindrome of the string given in the respective test case.

Constraints:
1 ≤ T ≤ 100
1 ≤ Str Length ≤ 104

Example:
Input:
1
aaaabbaa

Output:
aabbaa

Explanation:
Testcase 1: The longest palindrome string present in the given string is "aabbaa".

"""


#a = map(int,input().split())
#a = list(map(int,input().split()))

def palindrome(a):
    l = len(a)
    dp = [[0 for i in range(l)] for j in range(l)]
    # 
    max_len = 1
    start = 0
    for i in range(l):
        dp[i][i] = 1
    for i in range(l-1):
        j = i+1
        if a[i]==a[j]:
            dp[i][j] = 1
            if max_len<2:
                start = i
                max_len = 2
    for word in range(2,l+1):
        for t in range(l-word+1):
            j = t + word -1
            if a[t]==a[j] and dp[t+1][j-1]:
                dp[t][j] = 1
                if word>max_len:
                    max_len = word
                    start = t
    
    return a[start:start+max_len]
            
            
                
            

test = int(input())
for i in range(test):
    a = input()
    print(palindrome(a))
