from collections import deque

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    # 標記目前節點為已拜訪
    visited.add(start)
    print(start, end=" ")

    # 依序拜訪相鄰節點
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # 為了維持和遞迴類似順序，反向加入
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

def bfs_traverse(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)