#https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1/
def dfsHelp(g,k,visited):
    visited[k] = 1
    print(k,end=" ")
    for i in g[k]:
        if not visited[i]:
            dfsHelp(g,i,visited)       
def dfs(g,N):
    visited = [0 for i in range(N)]
    dfsHelp(g,0,visited)
