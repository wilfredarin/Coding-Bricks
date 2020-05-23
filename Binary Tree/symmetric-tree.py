#https://practice.geeksforgeeks.org/problems/symmetric-tree/1


def isMirror(r1,r2):
    if r1 is None and r2 is None:
        return 1
    if r1 is not None and r2 is not None:
        if r1.data==r2.data:
            return isMirror(r1.left,r2.right) and isMirror(r1.right,r2.left)
    return 0
        
        
    
def isSymmetric(root):
    if root is None:
        return 1
    return isMirror(root,root)   
    

