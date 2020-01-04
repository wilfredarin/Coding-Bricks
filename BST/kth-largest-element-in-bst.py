def helps(root,a):
    if not root:
        return
    helps(root.left,a)
    a.append(root.data)
    helps(root.right,a)
def kthLargest(root, k):
    a=[]
    helps(root,a)
    a.reverse()
    print(a[k-1])
