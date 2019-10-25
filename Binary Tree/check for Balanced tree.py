def height(a):
	if a is None:
		return 1
	l = height(a.left)
	r = height(a.right)
	if l>r:
		return l+1
	else:
		return r+1

def isBalanced(root):
	if root is None: return True
	
	if (abs(height(root.left)-height(root.right))<=1) and isBalanced(root.left) and isBalanced(root.right):
	    return True
	return False
