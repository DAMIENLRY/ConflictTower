from queue import Queue

def display_graph(graph):
    for y,x in graph:
        print(str((y,x))+" : "+str(graph[(y,x)]))


def create_adjacency_list_from_list(grid):
    graph = {}

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != -1:
                node = (i,j)
                graph[node] = []

                #check adjacent neighbours : up, down, left, right
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]:
                    xi, xj = i+di, j+dj

                    if (xi>=0 and xi<len(grid)) and (xj>=0 and xj<len(grid[i]) and grid[xi][xj] != -1):
                        graph[node].append((xi,xj))
    return graph


def find_shortest_path(backtrack_paths, target_node):
    if not backtrack_paths: return []
    shortest_path = []
    current = target_node

    while current is not None:
        shortest_path.append(current)
        current = backtrack_paths[current]

    shortest_path.reverse()
    return shortest_path


def breadth_first_search(adjacency_list, start, end):
    visited = {start: None}
    q = Queue()
    q.put(start)

    while not q.empty():
        element = q.get()

        values = adjacency_list[element]
        for v in values:
            if(v not in visited):
                visited[v] = element #add visited node and keep track of predecessor, to finally build the shortest path using backtracking
                if v==end:
                    return visited
                q.put(v)
    return False

def path_to_tower(start,end):
    map = [[1 for j in range(13)] for i in range(21)]
    for i in range(13):
        if i not in (2,3,9,10):
            map[10][i] = -1

    adjacency_list = create_adjacency_list_from_list(map)
    bfs = breadth_first_search(adjacency_list,start,end)
    shortest_path = find_shortest_path(bfs,end)
    return shortest_path
