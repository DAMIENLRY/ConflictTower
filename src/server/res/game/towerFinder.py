from queue import Queue
from typing import List, Union

def display_graph(graph) -> None:
    """
    Display the nodes and their neighbors in the graph.

    Args:
        graph (dict): The graph represented as a dictionary.

    Returns:
        None
    """
    for y, x in graph:
        print(str((y, x)) + " : " + str(graph[(y, x)]))


def create_adjacency_list_from_list(grid) -> dict:
    """
    Create an adjacency list from a 2D grid.

    Args:
        grid (list): The 2D grid.

    Returns:
        dict: The adjacency list.
    """
    graph = {}

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != -1:
                node = (i, j)
                graph[node] = []

                # Check adjacent neighbors: up, down, left, right, diagonals
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                    xi, xj = i + di, j + dj

                    if (0 <= xi < len(grid)) and (0 <= xj < len(grid[i]) and grid[xi][xj] != -1):
                        graph[node].append((xi, xj))
    return graph


def find_shortest_path(backtrack_paths, target_node) -> List[tuple[int]]:
    """
    Find the shortest path from the start node to the target node.

    Args:
        backtrack_paths (dict): Dictionary containing backtracking information.
        target_node: The target node to reach.

    Returns:
        list: The shortest path.
    """
    if not backtrack_paths:
        return []
    shortest_path = []
    current = target_node

    while current is not None:
        shortest_path.append(current)
        current = backtrack_paths[current]

    shortest_path.reverse()
    return shortest_path


def breadth_first_search(adjacency_list, start, end) -> Union[dict, bool]:
    """
    Perform Breadth-First Search to find the shortest path between two nodes.

    Args:
        adjacency_list (dict): The adjacency list representing the graph.
        start: The starting node.
        end: The target node.

    Returns:
        dict or False: Dictionary containing backtracking information or False if no path is found.
    """
    visited = {start: None}
    q = Queue()
    q.put(start)

    while not q.empty():
        element = q.get()
        values = adjacency_list[element]
        for v in values:
            if v not in visited:
                visited[v] = element  # Add visited node and keep track of predecessor, to finally build the shortest path using backtracking
                if v == end:
                    return visited
                q.put(v)
    return False

def path_to_tower(start, end) -> List[tuple[int]]:
    """
    Find the shortest path from the start node to the target node on a predefined map.

    Args:
        start: The starting node.
        end: The target node.

    Returns:
        list: The shortest path.
    """
    map = [[1 for j in range(13)] for i in range(21)]
    for i in range(13):
        if i not in (2, 3, 9, 10):
            map[10][i] = -1

    adjacency_list = create_adjacency_list_from_list(map)
    bfs = breadth_first_search(adjacency_list, start, end)
    shortest_path = find_shortest_path(bfs, end)
    return shortest_path
