from collections import deque


def bfs(graph, start, visited):
    # using deque library so that implementing Queue
    queue = deque([start])
    # mark a current node as visited
    visited[start] = True
    # iterate until queue is empty
    while queue:
        # print visited element
        v = queue.popleft()
        print(v, end=' ')
        # insert adjacent elements to queue
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
