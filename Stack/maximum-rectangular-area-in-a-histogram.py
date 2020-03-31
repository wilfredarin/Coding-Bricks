"""
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.

Input:
The first line contains an integer 'T' denoting the total number of test cases. T test-cases follow. In each test cases, the first line contains an integer 'N' denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array. The elements of the array represents the height of the bars.

Output:
For each test-case, in a separate line, the maximum rectangular area possible from the contiguous bars.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= A[i] <= 1018

Example:
Input: 
2
7
6 2 5 4 5 1 6
4
6 3 4 2
Output:
12
9
"""
#a = map(int,input().split())
#a = list(map(int,input().split()))


def maxArea(a):
    n = len(a)
    stack = []
    area = 0
    max_area = -1
    i = 0
    while i<n: 
        
        if not stack or a[stack[-1]]<=a[i]:
            stack.append(i)
            i+=1
        else:
            while stack and a[stack[-1]]>a[i]:
                index = stack.pop()
                if stack:
                    area = a[index]*(i-stack[-1]-1)
                    max_area = max(area,max_area)
                    
                else:
                    area = a[index]*i
                    max_area = max(area,max_area)
    
    while stack:
        index = stack.pop()
        if stack:
            area = a[index]*(i-stack[-1]-1)
            max_area = max(area,max_area) 
        else:
            area = a[index]*i
            max_area = max(max_area,area)
    return max_area
            
        
        
        
    
test = int(input())
for i in range(test):
    k = int(input())
    a = list(map(int,input().split()))
    print(maxArea(a))
