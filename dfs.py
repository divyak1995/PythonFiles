def DFS(vertex):
    if not visited[vertex]:
        visited[vertex]=True
        for neighbor in graph[vertex]:
            DFS(neighbor)
        outputStack.append(vertex)
        
graph = { 1 : set([2]), 2: set([4]), 3: set([2]), 4:set([5]), 5:set([]) , 6: set([7]), 7 :set([]) }
visited=dict()
for i in graph.keys():
    visited[i]=False
outputStack=[]
    
for vertex in graph.keys():
    DFS(vertex)
print outputStack
