def height(a):
	if a is None:
		return 1
	l = height(a.left)
	r = height(a.right)
	if l>r:
		return l+1
	else:
		return r+1

def printLevel(root,level,a):
	if root is None:
		return
	if level==1:
		a.append(root.data)
	printLevel(root.left,level-1,a)
	printLevel(root.right,level-1,a)

def sub(root):
	if root is None: return
	n = height(root)
	a = []
	for i in range(n):
		printLevel(root,i,a)
	return a

def isSubTree(T1, T2):
    # Code here
    l1,l2 = sub(T1),sub(T2)
    le1 = len(l1)
    le2 = len(l2)
    if le1>le2:
        if l1[le1-le2:le1]==l2:
            return True
    else: 
        if l2[le2-le1:le2]==l1:
            return True
    return False
