"""
Given a binary tree of size N, your task is to complete the function zigZagTraversal(), that prints the nodes of binary tree in ZigZag manner.

For Example:
For the below binary tree the zigzag order 
traversal will be 1 3 2 7 6 5 4.

Binary Tree Example
Input:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:


For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
For each test case print on a new line space-separated all the nodes of the tree in ZigZag manner.

Constraints:
1 <= T <= 100
1 <= N <= 104

Example:
Input:
2
3 2 1
7 7 9 8 8 6 N 10 9
Output:
3 1 2
7 9 7 8 8 6 9 10

Explanation:
Testcase 1: Given tree is
                         3
                      /       \
                    2        1
Hence the zigzag traversal will be 3 1 2.
Testcase 2: Given tree is 
                           7
                       /        \
                    9           7
                /        \      /     \
               8        8    6     N
            /      \
          10     9  
Hence the zigzag traversal will be 7 9 7 8 8 6 9 10.
"""

#### Method 1
def height(root):
    if root is None:
        return 0
    l = height(root.left)
    r = height(root.right)
    if l>r:
        return l+1
    else:
        return r+1
def help(root,level,array):
    if root is None:
        return 
    if level ==1:
        array.append(root.data)
    else:
        help(root.left,level-1,array)
        help(root.right,level-1,array)
        
def zigZagTraversal(root):
    n = height(root)
    for i in range(1,n+1):
        array = []
        help(root,i,array)
        if i%2==0:
            array.reverse()
            for i in array:
                print(i,end=" ")
        else:
            for i in array:
                print(i,end=" ")
                
                
###################   Method 2 ##########################

def zigZagTraversal(root):
    '''
    param: root:   root of tree
    return None, no need to print new line
    
    '''
    if root is None:
        return 
    next_level = []
    curr_level = [root]
    direction = True
    while curr_level:
        node = curr_level.pop()
        print(node.data,end=" ")
        if direction:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        else:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)
        if not curr_level:
            direction  = not direction
            curr_level = next_level
            next_level = []
            
