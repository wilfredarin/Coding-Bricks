def check_small(board,row,col,num):
	s_c = row-row%3
	s_r = col-col%3
	for i in range(3):
		for j in range(3):
			if board[s_c+i][s_r+j]==num:
				return False
	return True

def check_rc(board,row,col,num):
	if num in board[row]:
		return False
	for i in range(9):
		if board[i][col]==num:
			return False
	return True

def check_ful(board):
	for i in range(9):
		for j in range(9):
			if board[i][j]==0:
				return False

	return True
def check_place(board,l):
	for i in range(9):
		for j in range(9):
			if board[i][j]==0:
				l[0] = i
				l[1] = j
				return
			

def safe(board,row,col,num):
	if not board[row][col] and check_rc(board,row,col,num) and check_small(board,row,col,num):
		return True
	return False

def util(board):

	l = [0,0]
	s = ""
	if check_ful(board) :
		for i in board:
			for j in i:
			    s+=str(j)+" "
		print(s)
		return True
	check_place(board,l)
	row = l[0]
	col = l[1]
	for j in range(1,10):
		if safe(board,row,col,j):
			board[row][col]=j
			if util(board):
				return True
			board[row][col]=0
	return False

def st(a,matrix):
    num = 81
    c = 0
    for i in a:
        if i==" ":
            pass
        else:
            matrix[c//9][c%9]=int(i) 
            c+=1

            



n  = int(input())

for i in range(n):
    matrix = input()
    ma = [[0 for i in range(9)] for i in range(9)]
    st(matrix,ma)
    util(ma)

