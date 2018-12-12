output_queue=[]
def BFS(vertex):
    if not visited[vertex]:
        visited[vertex]=True
        queue.append(vertex)
        while queue: 
          s = queue.pop(0) 
          print (s, end = " ") 
          for i in graph[s]: 
              if visited[i] == False: 
                  queue.append(i) 
                  visited[i] = True
        
        
graph = { 1 : set([2,5]), 2: set([3,4]), 3:set([]),4:set([]), 5:set([6,7]) , 6: set([]), 7 :set([]) }
visited=dict()
for i in graph.keys():
    visited[i]=False
queue=[]
    
for vertex in graph.keys():
    BFS(vertex)
for i in range(len(output_queue)):
    print(output_queue[i],end = ' ')
