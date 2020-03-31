"""
Given a string S that represents column title of an Excel sheet, find the number that represents that column.
In excel A column is number 1, AA is 27 and so on.

Input:
The first line contains an integer T, depicting total number of test cases. T testcases follow. Each testcase contains a single line of input containing string S.

Output:
For each testcase, in a new line, print the column number.

Constraints:
1 ≤ T ≤ 100
1 ≤ |S| <=7

Example:
Input
2
A
AA
Output
1
27
"""

#a = map(int,input().split())
#a = list(map(int,input().split()))

test = int(input())
for i in range(test):
    l = list(input())
    ans = 0
    power = 0
    while l:
        ans+=(ord(l.pop())-64)*(26**power)
        power+=1
    print(ans)
        
    
    
