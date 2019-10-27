def height(root):
	if root is None:
		return 0
	l = height(root.left)
	r = height(root.right)
	if l>r:
		return (l+1)
	else:
		return (r+1)
def Levelwise(root,level,a):
	if root is None:
		return 
	elif level ==1:
		a.append(root)
	Levelwise(root.left,level-1,a)
	Levelwise(root.right,level-1,a)
def spiral(root):
	n = height(root)
	for i in range(n):
		a = []
		Levelwise(root,i+1,a)
		for i in range(len(a)-1):
			j=i+1
			a[i].nextRight =a[j]

def connect(root):
    '''
    :param root: root of the given tree
    :return: none, just connect accordingly.
    {
        # Node Class:
        class Node:
            def __init__(self,val):
                self.data = val
                self.left = None
                self.right = None
                self.nextRight = None
    }
    '''
    spiral(root)
