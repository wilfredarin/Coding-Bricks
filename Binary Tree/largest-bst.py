#https://practice.geeksforgeeks.org/problems/largest-bst/1
INT_MIN = -2147483648
INT_MAX = 2147483647
# Return the size of the largest sub-tree which is also a BST
def largestBst(root):
    a =largest(root)
    return a[4]
def largest(root):
    #code here
    if root is None:
        return ([True,0,INT_MIN,INT_MAX,0])
    if root.left is None and root.right is None:
        return ([True, 1, root.data, root.data,1])
    l = largest(root.left)
    r = largest(root.right)
    
    ret = [0,0,0,0,0]
    ret[1] = 1 + l[1] +r[1]
    if (l[0] and r[0] and l[2]<root.data and r[3]>root.data):
        ret[3] = min(l[3],r[3],root.data)
        ret[2] = max(l[2],r[2],root.data)
        ret[0] = True
        ret[4] = ret[1]
        return ret
    ret[4] = max(l[4],r[4])
    ret[0] =  False
    return ret
    
