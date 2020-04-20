#https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1/

def bfs(g,N):
    '''
    can use queue module already imported
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the bfs of the graph from node 0, newline is given by driver code
    '''
    queue = [0]
    visited = [0 for i in range(N)] #here is why it's different from tree
    visited[0] = 1
    while queue:
        a = queue.pop(0)
        print(a,end=" ")
        for node in g[a]:
            if not visited[node]:
                queue.append(node)
                visited[node] = 1
