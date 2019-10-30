class Node:
     def __init__(self,data):
          self.data = data
          self.left = left
          self.right = right

class Tree:
     def __init__(self,l):
          self.l = l
          self.root = self.makeTree()
     def makeTree(self):
          nodes = self.l
          n = len(nodes)
          root = Node(int(nodes[0]))
          for p in range(0,n,3):
               c = p+1
               di = nodes[c+1]
               parent = Node(int(nodes[p]))
               child = Node(int(nodes[c]))
               temp = root
               q = [root]
               while q and temp.data!=parent.data:
                    temp = q.pop(0)
                    if temp.left:
                         q.append(temp.left)
                    if temp.right:
                         q.append(temp.right)
               if di =="R":
                    temp.right = child
               else:
                    temp.left = child
          return root
     def print(self):
          if self.root is None:
               return ""
          root = self.root
          q = [root]
          while q:
               temp = q.pop(0)
               if temp.left:
                    q.append(temp.left)
               else:
                    q.append(temp.right)
               print(temp,end=" ")

t = Tree(input())
t.print()
# My input : [10 20 L 10 30 R 20 40 L 20 60 R]

