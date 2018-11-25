from collections import defaultdict

n,m=map(int,raw_input().split())

adjacency_list=defaultdict(list)

for i in range(m):
    x,y=map(str,raw_input().split())
    adjacency_list[x].append(y)
    
print adjacency_list


visited_list = defaultdict()
for i in range(1, n+1):
    visited_list[str(i)]=False
    
output_stack=[]

def topology_sort(vertex):
    if not visited_list[vertex]:
        visited_list[vertex] = True
        for neighbor in adjacency_list[vertex]:
            topology_sort(neighbor)
        output_stack.insert(0, vertex)
        
        
        
for vertex in visited_list:
    topology_sort(vertex)

for i in output_stack:
    print i,
