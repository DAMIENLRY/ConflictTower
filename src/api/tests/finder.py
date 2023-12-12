import unittest
from io import StringIO
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from towerFinder import createAdjacencyListFromList, findShortestPath, breadthFirstSearch, pathToTower

class TestTowerFinder(unittest.TestCase):

    def test_createAdjacencyListFromList(self):
        grid = [[0, 1], [1, 0]]
        graph = createAdjacencyListFromList(grid)
        expected_graph = {(0, 0): [(1, 0), (0, 1), (1, 1)], (0, 1): [(1, 1), (0, 0), (1, 0)], (1, 0): [(0, 0), (1, 1), (0, 1)], (1, 1): [(0, 1), (1, 0), (0, 0)]}
        self.assertEqual(graph, expected_graph)

    def test_findShortestPath(self):
        backtrackPaths = {(0, 0): None, (1, 0): (0, 0), (0, 1): (0, 0), (1, 1): (0, 1)}
        targetNode = (1, 1)
        shortestPath = findShortestPath(backtrackPaths, targetNode)
        expected_shortestPath = [(0, 0), (0, 1), (1, 1)]
        self.assertEqual(shortestPath, expected_shortestPath)
    
    def test_breadthFirstSearch(self):
        adjacencyList = {(0, 0): [(1, 0), (0, 1), (1, 1)], (0, 1): [(1, 1), (0, 0), (1, 0)], (1, 0): [(0, 0), (1, 1), (0, 1)], (1, 1): [(0, 1), (1, 0), (0, 0)]}
        start = (0, 0)
        end = (1, 1)
        bfs = breadthFirstSearch(adjacencyList, start, end)
        expected_bfs = {(0, 0): None, (1, 0): (0, 0), (0, 1): (0, 0), (1, 1): (0, 0)}
        self.assertEqual(bfs, expected_bfs)

    def test_pathToTower(self):
        start = (0, 0)
        end = (1, 1)
        path = pathToTower(start, end)
        expected_path = [(0, 0), (1, 1)]
        self.assertEqual(path, expected_path)

if __name__ == '__main__':
    unittest.main()