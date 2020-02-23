"""

Valid Substring Submissions: 12220   Accuracy: 43.83%   Difficulty: Easy   Marks: 2
           
Problems
Given a string S consisting only of opening and closing parenthesis 'ie '('  and ')', find out the length of the longest valid substring.

NOTE: Length of smallest the valid substring ( ) is 2.

 

Input
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
The first line of each test case contains a string S consisting only of ( and ).


Output

Print out the length of the longest valid substring.

Constraints
1 <= T <= 100
0 <   S  <= 110

 

Examples 

Input
4
(()(
()()((
((()()())))
()(())(

Output
2
4
10
6
"""
def longestValidParentheses(A):
    stack = [-1]
    ans = 0
    n = len(A)
    for i in range(n):
        if A[i]=="(":
            stack.append(i)
        else:
            stack.pop()
            if stack:
                ans = max(ans,i-stack[-1])
            else:
                stack.append(i)
    return ans
test = int(input())
for e in range(test):
    A = input()
    print(longestValidParentheses(A))


