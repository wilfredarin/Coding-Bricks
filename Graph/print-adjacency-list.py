#https://practice.geeksforgeeks.org/problems/print-adjacency-list/0

#a = map(int,input().split())
#a = list(map(int,input().split()))

test = int(input())
for i in range(test):
    v,e = map(int,input().split())
    graph = {}
    for node in range(e):
        s,d = input().split()
        if s not in graph:
            graph[s] = [d]
        elif s in graph:
            graph[s].append(d)
        if d not in graph:
            graph[d] = [s]
        else:
            graph[d].append(s)
    
    for w in range(v):
        ans= ""
        ans+=str(w)+'-> '
        if str(w) in graph:
            ans+='-> '.join(graph[str(w)])
            print(ans)
        else:
            print(str(w))
        
