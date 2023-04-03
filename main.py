from collections import deque

def bfs(graph, start, output=print):
    visited = set()
    queue = deque([start])
    bfs_number = {start: 0}
    bfs_counter = 1
    output("vertex\tBFS \tQueue")
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            bfs_number[vertex] = bfs_counter
            bfs_counter += 1
            queue.extend(graph[vertex] - visited)
        output(f"{vertex}\t\t{bfs_number[vertex]}\t\t{list(queue)}")


if __name__ == '__main__':
    graph = {}
    filename = input("Enter graph file name: ")
    with open(filename) as f:
        for line in f:
            v1, v2 = map(int, line.split())
            if v1 not in graph:
                graph[v1] = set()
            if v2 not in graph:
                graph[v2] = set()
            graph[v1].add(v2)
            graph[v2].add(v1)


    start_vertex = int(input("Enter start vertex: "))


    bfs(graph, start_vertex)
