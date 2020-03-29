"""
Given a number N, your task is to complete the function which generates all n-bit grey code sequences, a grey code sequence is a sequence such that successive patterns in it differ by one bit.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N.

Output:
For each test case in print the generated grey code sequences separated by space.

Constraints:
1<=T<=10
1<=N<=10

Example(To be used for expected output):
Input:
2
2
1

Output:
00 01 11 10
0 1

"""
import copy
# Function should print all the Grey Code Generated
def generateCode(n):
    # Code here
    l1 = ["0","1"]
    l2 = []
    for i in  range(n-1):
        l2 = copy.copy(l1)
        l2.reverse()
        for e in range(len(l1)):
            l1[e]="0"+l1[e]
        for e  in range(len(l2)):
            l2[e]="1"+l2[e]
        l1 = l1+l2
    for i in range(len(l1)):
        print(l1[i],end=" ")
    print("")
        
