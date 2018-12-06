def isCyclic(graph):
    visited=set()
    path=set()
    def visit(vertex):
        if vertex in visited:
            return False
        visited.add(vertex)
        path.add(vertex)
        for neighbor in graph.get(vertex,()):
            if neighbor in path or visit(neighbor):
                return True
        path.remove(vertex)
        return False
    
    return any(visit(v) for v in graph)

output_stack=[]

def topology_sort(vertex):
    if not visited_list[vertex]:
        visited_list[vertex] = True
        for neighbor in graph[vertex]:
            topology_sort(neighbor)
        output_stack.insert(0, vertex)
  
    
graph = {'A': set(['B']),
         'B': set(['D']),
         'C': set(['B']), 
         'D': set(['E']),
         'E': set([])}

if isCyclic(graph):
  print('Graph is cyclic. Topological sort is not possible')
else:
  print('Given graph is a directed acyclic graph. Topological sort is possible ')
  visited_list = dict()
  for i in graph.keys():
      visited_list[i]=False
      
  for vertex in graph.keys():
      topology_sort(vertex)
  print('Topological sort of the graph is:')
  print(output_stack)
