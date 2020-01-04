'''
#first understand how the k value is given then solve the poblem
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''
# your task is to complete this function
# function should return kth smallest element from the BST
def k_smallest_element(root, n):
    # Code here
    T = 1
    while T:
        if n == root.key+1:
            #print(root.data)
            return (root.data)
        elif n > root.key+1:
            n = n-(root.key+1)
            root = root.right
            
        else:
            root = root.left
