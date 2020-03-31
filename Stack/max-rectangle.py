"""
Given a binary matrix, Your task is to complete the function maxArea which the maximum size rectangle area in a binary-sub-matrix with all 1’s. 
The function takes 3 arguments the first argument is the Matrix M[ ] [ ] and the next two are two  integers n and m which denotes the size of the matrix M. 
Your function should return an integer denoting the area of the maximum rectangle .

Input:
The first line of input is an integer T denoting the no of test cases . 
Then T test cases follow. The first line of each test case are 2 integers n and m denoting the size of the matrix M . Then in the next line are n*m space separated values of the matrix M.

Output:
For each test case output will be the area of the maximum rectangle .

Constraints:
1<=T<=100
1<=n,m<=1000
0<=M[][]<=1

Example:
Input
1
4 4 
0 1 1 0 1 1 1 1 1 1 1 1 1 1 0 0

Output
8

Explanation
For the above test case the matrix will look like
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
the max size rectangle is 
1 1 1 1
1 1 1 1
and area is 4 *2 = 8

"""

def maxArea(row):
    n = len(row)
    stack = []
    area = -1
    k = 0
    while k<n:
        if not stack or row[stack[-1]]<=row[k]:
            stack.append(k)
            k+=1
        else:
            while stack and row[stack[-1]]>row[k]:
                index = stack.pop()
                area = max(area,row[index]*(k-stack[-1]-1 if stack else k))
    while stack:
        index = stack.pop()
        area = max(area,row[index]*(k-stack[-1]-1 if stack else k))
    return area
def maxRectangle(A, R, C):
    output_area = -1
    histogram= [0 for i in range(C)]
    for i in range(R):
        row = A[i]
        for j in range(C):
            if row[j]:
                histogram[j]+=1
            else:
                histogram[j] =0
        output_area = max(output_area,maxArea(histogram))
    return output_area   
    
