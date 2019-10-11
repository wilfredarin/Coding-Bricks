
def isSafe(board, row, col,n): 

	# Check this row on left side 
	for i in range(col): 
		if board[row][i] == 1: 
			return False

	# Check upper diagonal on left side 
	for i, j in zip(range(row, -1, -1), 
					range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	# Check lower diagonal on left side 
	for i, j in zip(range(row, n, 1), 
					range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	return True

def solvenQUtil(board, col,ans,n,sol): 
	
	t=""
	if col >= n:
		for i in ans:
			t+=str(i)+" "
		sol.append(t)
				

	for i in range(n): 

		if isSafe(board, i, col,n): 
			
		
			board[i][col] = 1
			ans.append(i+1)

		 
			solvenQUtil(board, col + 1,ans,n,sol)

		
			board[i][col] = 0
			ans.pop()
def solvenQ(n): 
	
	ans=[]
	sol = []
	
	board = [[0 for i in range(n)] for j in range(n)]
	solvenQUtil(board, 0,ans,n,sol)
	if not sol:
	    return(print(-1))
	for i in sol:
		print("["+i+"]",end =" ")
	print("")
 

for i in range(int(input())):
    n = int(input())
    solvenQ(n)

