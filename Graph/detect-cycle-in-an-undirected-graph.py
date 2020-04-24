#https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

def isCycle(p, g,visited,parent):
    visited[p] = 1
    for nbr in g[p]:
        if not visited[nbr]:
            if isCycle(nbr,g,visited,p):
                return 1
        elif nbr!=parent:
            return 1
    return 0
def isCyclic(g,n):
    # code herea
    visited = [0 for i in range(n)]
    for i in range(n):
        if not visited[i]:
            if isCycle(i,g,visited,-1):
                return 1
    return 0
