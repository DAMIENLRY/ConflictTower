from queue import Queue
from turtle import back


def displayGraph(graph):
    for y,x in graph:
        print(str((y,x))+" : "+str(graph[(y,x)]))


def createAdjacencyListFromList(grid):
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


def findShortestPath(backtrackPaths, targetNode):
    shortestPath = []
    current = targetNode

    while current is not None:
        shortestPath.append(current)
        current = backtrackPaths[current]

    shortestPath.reverse()
    return shortestPath


def breadthFirstSearch(adjacencyList, start, end):
    visited = {start: None}    
    q = Queue()
    q.put(start)

    while not q.empty():
        element = q.get()

        values = adjacencyList[element]
        for v in values:
            if(v not in visited):
                visited[v] = element #add visited node and keep track of predecessor, to finally build the shortest path using backtracking
                if v==end:
                    return visited
                q.put(v)
    return False

def find():
    map = [[1 for j in range(13)] for i in range(21)]
    for i in range(13):
        if i not in (2,3,9,10):
            map[10][i] = -1

    adjacencyList = createAdjacencyListFromList(map)
    #print(adjacencyList)

    bfs = breadthFirstSearch(adjacencyList,(20,12),(4,6))
    #print(bfs)
    
    shortestPath = findShortestPath(bfs,(4,6))
    print(shortestPath)
    return shortestPath