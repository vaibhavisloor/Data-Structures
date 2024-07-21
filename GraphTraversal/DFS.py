def dfs(graph,start):
    visited=set()
    stack=[start]

    while stack:
        node=stack.pop()
        if node not in visited:
            visited.add(node)

            stack.extend(reversed(graph[node]))
    print(visited)    


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph,"A")


# uses stack and visited set
# pop from stack and check if it is visited
# if not add to visited and append the neighbours list by reversing it.