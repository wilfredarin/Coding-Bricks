#https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1
def minWt(wt,vis,V):
    mi = float("inf")
    for node in range(V):
        if wt[node]<mi and not vis[node]:
            mi = wt[node]
            min_index = node
    return min_index        
    
def spanningTree(V, E, graph):
    #code here
    weight = [float("inf")]*V
    parent = [None]*V
    weight[0] = 0
    visited = [False]*V
    parent[0] = -1
    for vertex in range(V):
        min_node = minWt(weight,visited,V) 
        visited[min_node]=1
        for nbr in range(V):
            if graph[min_node][nbr]!=float("inf") and not visited[nbr] and weight[nbr]>graph[min_node][nbr]:
                weight[nbr] = graph[min_node][nbr]
                parent[nbr] = vertex
    return (sum(weight))     
