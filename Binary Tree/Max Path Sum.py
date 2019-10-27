def look(root):
	if root is None: 
		return 0
	return (max(look(root.left),look(root.right))+root.data)
    
def best(root):
    pass
    
def maxPathSum(root):
    #Your code here
    q = [root]
    ans = 0
    while q:
        temp = q.pop(0)
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)
        ans =max(ans,look(temp.right)+look(temp.left)+temp.data)
    return ans
