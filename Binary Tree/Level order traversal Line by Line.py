def height(root):
    if root==None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    if lh>rh:
        return lh+1
    else:
        return rh +1

def levelPrint(root,level):
    if root==None:
        return
    if level==1:
        print(root.data,end=" ")
        a.append(root.data)
    else:
        levelPrint(root.left,level-1)
        levelPrint(root.right,level-1)
def levelOrder(node):
    h = height(node)
    for i in range(h):
        levelPrint(node,i+1)
        print("$",end=" ")
