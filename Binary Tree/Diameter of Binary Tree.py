def height(root):
	if root is None:
		return 0
	l = height(root.left)
	r = height(root.right)
	if l>r:
		return (l+1)
	else:
		return (r+1)
def diameter(root):
	ans = 0
	q = [root]
	while q:
		temp = q.pop(0)
		if temp.left:
			q.append(temp.left)
		if temp.right:
			q.append(temp.right)
		ans = max(ans,height(temp.left)+height(temp.right)+1)
	return ans
