# DFS implementation using python

'''  
    Consider the following Graph for DFS implementation
    
                   10                   
                  /  \   
                20     30
              /  \       \ 
            40    50  ---> 60
            
'''

Graph = {
    # Creating a dictornary of parent node and their corresponding child nodes

    '10': ['20', '30'],
    '20': ['40', '50'],
    '30': ['60'],
    '40': [],
    '50': ['60'],
    '60': []
}

# Set to keep note of visited nodes.
visited = set()


def dfs(visited, Graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour_node in Graph[node]:
            dfs(visited, Graph, neighbour_node)


# calling DFS function
dfs(visited, Graph, '10')
