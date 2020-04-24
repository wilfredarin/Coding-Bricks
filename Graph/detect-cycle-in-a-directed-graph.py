#https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
def isCycle(v,graph,visited,stack):
    visited[v] = 1
    stack[v] = 1
    for nbr in graph[v]:
        if not visited[nbr]:
            if isCycle(nbr,graph,visited,stack):
                return True
        elif stack[nbr]:
            return True
    stack[v] = 0
    return False
            
def isCyclic(n, graph):
    # Code here
    visited = [0 for i in range(n)]
    stack =[0 for i in range(n)]
    
    for v in range(n):
        if not visited[v]:
            if isCycle(v,graph,visited,stack):
                return True
    return False
