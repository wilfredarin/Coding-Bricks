def size(a):
	if a is None:
		return 0
	return (size(a.left)+size(a.right)+1)
