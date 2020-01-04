def helps(root,a):
    if not root:
        return
    helps(root.left,a)
    a.append(root.data)
    helps(root.right,a)
def inorder(root):
    # Code here
    a = []
    helps(root,a)
    return a
def leaf(root,b):
    if root is None:
        return
    leaf(root.left,b)
    if (root.left is None) and root.right is None:
        b.append(root.data)
    leaf(root.right,b)
def isdeadEnd(root):
    # Code here
    a = inorder(root)
    a = [0] + a + [0]
    b = []
    leaf(root,b)
    #print(a,b)
    T = True
    while b and T:
        p = b.pop(0)
        i = a.index(p)
        if a[i] == a[i-1]+1 and a[i+1]==a[i]+1:
            T=False
    if not T:
        return(1)
    else:
        return(0)
