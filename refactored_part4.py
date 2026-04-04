from abc import ABC, abstractmethod
from typing import List, Dict
from experiment1_part1 import dijkstra, bellman_ford, mystery
from search_algs import a_star


class Graph(ABC):
    @abstractmethod
    def get_adj_nodes(self, node: int) -> List[int]:
        pass

    @abstractmethod
    def add_node(self, node: int):
        pass

    @abstractmethod
    def add_edge(self, start: int, end: int, weight: float):
        pass

    @abstractmethod
    def get_num_of_nodes(self) -> int:
        pass

    @abstractmethod
    def w(self, node1: int, node2: int) -> float:
        pass


class SPAlgorithm(ABC):
    @abstractmethod
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        pass


class WeightedGraph(Graph):
    def __init__(self):
        self.adj = {}
        self.weights = {}

    def get_adj_nodes(self, node: int) -> List[int]:
        return self.adj.get(node, [])

    def add_node(self, node: int):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, start: int, end: int, weight: float):
        self.add_node(start)
        self.add_node(end)
        if end not in self.adj[start]:
            self.adj[start].append(end)
        self.weights[(start, end)] = weight

    def get_num_of_nodes(self) -> int:
        return len(self.adj)

    def w(self, node1: int, node2: int) -> float:
        return self.weights.get((node1, node2), float("inf"))


class HeuristicGraph(WeightedGraph):
    def __init__(self):
        super().__init__()
        self.heuristic: Dict[int, float] = {}

    def get_heuristic(self) -> Dict[int, float]:
        return self.heuristic


class Dijkstra(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        return dijkstra(graph, source, dest)


class Bellman_Ford(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        distances = bellman_ford(graph, source)
        return distances[dest]
    

class A_Star(SPAlgorithm):
    def calc_sp(self, graph: HeuristicGraph, source: int, dest: int) -> float:
        return a_star(graph, source, dest, graph.get_heuristic())
    

class ShortPathFinder:
    def __init__(self):
        self.graph: Graph = None
        self.algorithm: SPAlgorithm = None

    def calc_short_path(self, source: int, dest: int) -> float:
        if self.graph is None or self.algorithm is None:
            raise ValueError("Graph or algorithm is not properly set.")
        return self.algorithm.calc_sp(self.graph, source, dest)

    def set_graph(self, graph: Graph):
        self.graph = graph

    def set_algorithm(self, algorithm: SPAlgorithm):
        self.algorithm = algorithm