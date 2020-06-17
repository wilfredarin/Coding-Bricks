#https://practice.geeksforgeeks.org/problems/merge-two-bst-s/1
def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)

def merge(root1, root2):
    arr1 = []
    arr2 = []
    inorder(root1,arr1)
    inorder(root2,arr2)
    #code here.
    return sorted (arr1 + arr2)
