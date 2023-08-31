#BFS implementation using python

'''  
    Consider the following Graph for BFS implementation
    
                   10                   
                  /  \   
                20     30
              /  \       \ 
            40    50  ---> 60
            
'''

Graph = {
  #Creating a dictornary of parent node and their corresponding child nodes

  '10' : ['20','30'],
  '20' : ['40', '50'],
  '30' : ['60'],
  '40' : [],
  '50' : ['60'],
  '60' : []
}

 #  A list to keep note of visited nodes.
visited = []

#Initialize a queue
queue = []    

def bfs(visited, Graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour_node in Graph[s]:
      if neighbour_node not in visited:
        visited.append(neighbour_node)
        queue.append(neighbour_node)

#Calling the function
bfs(visited, Graph, '10')