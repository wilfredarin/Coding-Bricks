"""
You are given a tree and you need to do the level order traversal on this tree.
Level order traversal of a tree is breadth-first traversal for the tree.



Level order traversal of above tree is 1 2 3 4 5

Input:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
The function should print the level order traversal of the tree as specified in the problem statement.

Your Task:
You don't have to take any input. Just complete the function levelOrder() that takes node as parameter and prints the level order. The newline is automatically appended by the driver code.

Constraints:
1 <= T <= 100
1 <= Number of nodes<= 104
1 <= Data of a node <= 104

Example:
Input:
2
1 3 2
10 20 30 40 60 N N
Output:
1 3 2
10 20 30 40 60

Explanation:
Testcase1: The tree is
        1
     /      \
   3       2
So, the level order would be 1 3 2
Testcase2: The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
So, the level order would be 10 20 30 40 60

"""


#method using QUEUE
def levelOrder(root):
    if root is None:
        return 
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data,end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return queue
    
    
#method 2

def levelOrder(root):
   def height(root):
          if root is None:
              return 0
          l = height(root.left)
          h = height(root.right)
          if l>h:
              return l+1
          else:
              return h+1

      def help(root,level):
          if root is None:
              return 
          if level==1:
              print(root.data,end=" ")
          else:
              help(root.left,level-1)
              help(root.right,level-1)

      n = height(root)
      for i in range(1,n+1):
          help(root,i)
        
    
        
