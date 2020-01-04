def printNearNodes(root,l,h):
    #Your code here
    if not root:
        return
    printNearNodes(root.left,l,h)
    if root.data >= l and root.data<=h:
        print(root.data,end=" ")
    printNearNodes(root.right,l,h)
