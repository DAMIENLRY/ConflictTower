# camp : 33 (largeur) x 24 (hauteur)
# camps : 33 x 24*2 = 33 (largeur) + 48 (hauteur)

# rivière : 33 (largeur) x 2 (hauteur)

# carte : 33 (largeur) + 50 (hauteur)

def createGraphFromGrid(grid):
    graph = {}

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != -1:
                node = (i,j)
                graph[node] = []

                #check adjacent neighbours : up, down, left, right
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    xi, xj = i+di, j+dj

                    if (xi>=0 and xi<len(grid)) and(xj>=0 and xj<len(grid[i]) and grid[xi][xj] != -1):
                        graph[node].append((xi,xj))
    return graph

def displayGraph(graph):
    for y,x in graph:
        print(str((y,x))+" : "+str(graph[(y,x)]))

def dijkstra(graph, start, end):
    found = False

    path = []
    visited = []
    visited.append(start)

    display_graph(graph)

    for y,x in graph:
        if((y,x) not in visited): visited.append(y,x)

    return path

def main():
    #map = [[1 for j in range(33)] for i in range(50)]
    map = [
        [1,1,1,1],
        [1,-1,1,-1],
        [1,1,1,1],
        [-1,-1,-1,1],
        [1,1,1,1],
    ]

    graph = createGraphFromGrid(map)
    dij = dijkstra(graph, (4,0), (0,0))
    #print(map)

main()