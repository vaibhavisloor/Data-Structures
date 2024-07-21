from collections import deque

def bfs(graph,start):
    visited=set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                queue.append(neighbour)
    print(visited)        

if __name__ == "__main__":
    graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}
    
bfs(graph,0)    


# Uses queue and visited set
# pop left from queue and check if it is in visited
# if not then add to visited set and append the neighbours to queue one by one