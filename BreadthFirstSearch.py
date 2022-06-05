import collections


def bfs(graph, s):
    visited, queue = set(), collections.deque([s])
    visited.add(s)
    while queue:
        x = queue.popleft()
        print(str(x), end=" ")
        for neighbour in graph[x]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
