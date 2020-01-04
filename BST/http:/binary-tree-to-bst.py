def help(root,a):
    if root is None:
        return
    help(root.left, a)
    a.append(root.data)
    help(root.right, a)
    
def inorder(root,a):
    if root is None:
        return
    inorder(root.left,a)
    root.data =a.pop(0)
    inorder(root.right,a)
def binaryToBST(root):
    #Code here
    a = []
    help(root,a)
    a.sort()
    inorder(root,a)
    return root
    
