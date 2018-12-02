graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']), 
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

         
def recursive_dfs(graph, node):
    result = [node]
    seen = set(node)

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                result.append(neighbor)     # this line will be replaced below
                seen.add(neighbor)
                recursive_helper(neighbor)

    recursive_helper(node)
    return result

visited=recursive_dfs(graph, 'A') 
print visited
