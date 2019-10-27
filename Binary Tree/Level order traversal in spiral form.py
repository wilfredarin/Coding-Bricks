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
		a.append(int(root.data))
	Levelwise(root.left,level-1,a)
	Levelwise(root.right,level-1,a)

def spiral(root):
	n = height(root)
	for i in range(1,n+1):
		a = []
		if i==1 or i%2==0:
			Levelwise(root,i,a)
			for k in a:
				print(k,end=" ")
		else:
			Levelwise(root,i,a)
			a.reverse()
			for j in a:
				print(j,end=" ")

def printSpiralLevelOrder(root):
    # Code here
    spiral(root)
