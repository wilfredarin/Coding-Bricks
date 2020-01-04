def minNode(node):
    while node.left:
        node = node.left
    return node
        
def inorderSuccessor(root,node):
    temp = root
    while temp:
        if node.data<temp.data:
            temp = temp.left
        elif node.data>temp.data:
            temp = temp.right
        else:
            break
    node = temp

    if node.right:
        return minNode(node.right)
       
    suc = None
    while root != None:
        if node.data<root.data:
            suc = root
            root = root.left
        elif node.data>root.data:
            
            root = root.right
        else:
            break
    return suc
