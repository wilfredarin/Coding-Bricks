def insertinBST(root, node):
    # Code here
    if root is None or root.data ==node.data:
        return root
    else:
        if node.data<root.data:
            if root.left is None:
                root.left =node
            else:
                insertinBST(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                insertinBST(root.right,node)
        return root
