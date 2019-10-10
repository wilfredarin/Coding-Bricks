def safe(board,x,y,n):
    if x>=0 and y>=0 and x<n and y<n and board[x][y]:
        return True
    return False


def util(board,x,y,n,ans,track,path):
    if x==n-1 and y==n-1:
        ans.append(path)
    if safe(board,x+1,y,n) and (track[x+1][y] == 0) :
        track[x+1][y] = 1
        util(board,x+1,y,n,ans,track,path+"D")
    if safe(board,x-1,y,n) and track[x-1][y]==0 :
        track[x-1][y] = 1
        util(board,x-1,y,n,ans,track,path+"U")
    if safe(board,x,y+1,n) and track[x][y+1]==0 :
        track[x][y+1] = 1
        util(board,x,y+1,n,ans,track,path+"R")
    if safe(board,x,y-1,n) and track[x][y-1]==0 :
        track[x][y-1] = 1
        util(board,x,y-1,n,ans,track,path+"L")
    if safe(board,x,y,n):
        track[x][y]=0
        
def findPath(arr, n):
    # code here
    track = [[0 for i in range(n)] for j in range(n)]
    ans = []
    path=""
    track[0][0]=1
    util(arr,0,0,n,ans,track,path)
    ans.sort()
    answer = ""
    for i in ans:
        answer+=i+" "
    return answer
