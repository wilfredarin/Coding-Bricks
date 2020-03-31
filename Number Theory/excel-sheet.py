"""
Given a positive integer N, print its corresponding column title as it would appear in an Excel sheet.
For N =1 we have column A, for 27 we have AA and so on.

Note: The alphabets are all in uppercase.

Input:
The first line contains an integer T, depicting total number of test cases. Then following T lines contains an integer N.

Output:
For each testcase, in a new line, print the string corrosponding to the column number.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107

Example:
Input:
1
51
Output:
AY
 
"""

#a = map(int,input().split())
#a = list(map(int,input().split()))

test = int(input())
table = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(test):
    n = int(input()) 
    s = ""
    while n>0:
        r = n%26
        if r==0:
            s+="Z"
            n=n//26-1
        else:
            n=n//26
            s+=table[r-1]
    print(s[::-1])
