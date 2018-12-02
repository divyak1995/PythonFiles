graph = {'A': set(['B']),
         'B': set(['D']),
         'C': set(['B']), 
         'D': set(['E']),
         'E': set([])}

visited_list = dict()
for i in graph.keys():
    visited_list[i]=False
    
output_stack=[]

def topology_sort(vertex):
    if not visited_list[vertex]:
        visited_list[vertex] = True
        for neighbor in graph[vertex]:
            topology_sort(neighbor)
        output_stack.insert(0, vertex)
    
for vertex in graph.keys():
    topology_sort(vertex)

print output_stack
