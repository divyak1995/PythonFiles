def cyclic(g):
    path = set()
    visited = set()

    def visit(vertex):
        if vertex in visited:
            return False
        visited.add(vertex)
        path.add(vertex)
        for neighbour in g.get(vertex, ()):
            if neighbour in path or visit(neighbour):
                return True
        path.remove(vertex)
        return False

    return any(visit(v) for v in g)
    
    
graph = {1:set([2,3]), 2:set([3,1]), 3:set([8])}
print cyclic(graph)
