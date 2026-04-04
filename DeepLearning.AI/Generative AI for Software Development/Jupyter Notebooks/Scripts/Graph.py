# NOT GOOD FOR PRODUCTION
# class Graph:
#     def __init__(self, directed=False):
#         self.graph = {}
#         self.directed = directed
#
#     def add_vertex(self, vertex):
#         if vertex not in self.graph:
#             self.graph[vertex] = set()
#
#     def add_edge(self, src, dest):
#         if src not in self.graph:
#             self.add_vertex(src)
#         if dest not in self.graph:
#             self.add_vertex(dest)
#         self.graph[src].add(dest)
#         if not self.directed:
#             self.graph[dest].add(src)
#
#     def remove_edge(self, src, dest):
#         if src in self.graph:
#             if dest in self.graph[src]:
#                 self.graph[src].remove(dest)
#         if not self.directed:
#             if dest in self.graph and src in self.graph[dest]:
#                 self.graph[dest].remove(src)
#
#     def remove_vertex(self, vertex):
#         if vertex in self.graph:
#             # Remove any edges from other vertices to this one
#             for adj in list(self.graph):
#                 if vertex in self.graph[adj]:
#                     self.graph[adj].remove(vertex)
#             # Remove the vertex entry
#             del self.graph[vertex]
#
#     def get_adjacent_vertices(self, vertex):
#         if vertex in self.graph:
#             return self.graph[vertex]
#         else:
#             return []
#
#     def __str__(self):
#         return str(self.graph)
#
#
# # Example usage:
# g = Graph(directed=True)
# g.add_vertex('A')
# g.add_vertex('B')
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('Z', 'X')
# result = g.get_adjacent_vertices('A')
# print(g)
# print(result)



# BETTER SOLUTION FOR PRODUCTION
from typing import Dict, Set, Hashable, FrozenSet
import threading

class Graph:
    def __init__(self, directed: bool = False, max_vertices: int | None = None):
        self._graph: Dict[Hashable, Set[Hashable]] = {}
        self.directed = directed
        self.max_vertices = max_vertices
        self._lock = threading.RLock()
        self._edge_count = 0

    def _validate_vertex(self, vertex: Hashable) -> None:
        if vertex is None:
            raise ValueError("vertex cannot be None")
        try:
            hash(vertex)
        except TypeError as e:
            raise TypeError("vertex must be hashable") from e

    def add_vertex(self, vertex: Hashable) -> None:
        self._validate_vertex(vertex)
        with self._lock:
            if vertex not in self._graph:
                if self.max_vertices is not None and len(self._graph) >= self.max_vertices:
                    raise MemoryError("maximum number of vertices reached")
                self._graph[vertex] = set()

    def add_edge(self, src: Hashable, dest: Hashable) -> None:
        self._validate_vertex(src)
        self._validate_vertex(dest)

        with self._lock:
            if src not in self._graph or dest not in self._graph:
                raise KeyError("both vertices must exist before adding an edge")

            if dest not in self._graph[src]:
                self._graph[src].add(dest)
                self._edge_count += 1

            if not self.directed and src not in self._graph[dest]:
                self._graph[dest].add(src)

    def remove_edge(self, src: Hashable, dest: Hashable) -> bool:
        with self._lock:
            if src not in self._graph or dest not in self._graph:
                return False

            removed = dest in self._graph[src]
            if removed:
                self._graph[src].remove(dest)
                self._edge_count -= 1

            if not self.directed and src in self._graph[dest]:
                self._graph[dest].remove(src)

            return removed

    def remove_vertex(self, vertex: Hashable) -> bool:
        with self._lock:
            if vertex not in self._graph:
                return False

            # outgoing edges
            outgoing = len(self._graph[vertex])

            # incoming edges
            incoming = 0
            for other in self._graph:
                if other != vertex and vertex in self._graph[other]:
                    self._graph[other].remove(vertex)
                    incoming += 1

            del self._graph[vertex]

            if self.directed:
                self._edge_count -= (outgoing + incoming)
            else:
                self._edge_count -= outgoing

            return True

    def get_adjacent_vertices(self, vertex: Hashable) -> FrozenSet[Hashable]:
        with self._lock:
            if vertex not in self._graph:
                raise KeyError(f"vertex {vertex!r} not found")
            return frozenset(self._graph[vertex])

    def has_vertex(self, vertex: Hashable) -> bool:
        with self._lock:
            return vertex in self._graph

    def has_edge(self, src: Hashable, dest: Hashable) -> bool:
        with self._lock:
            return src in self._graph and dest in self._graph[src]

    def vertex_count(self) -> int:
        with self._lock:
            return len(self._graph)

    def edge_count(self) -> int:
        with self._lock:
            return self._edge_count

    def __contains__(self, vertex: Hashable) -> bool:
        return self.has_vertex(vertex)

    def __len__(self) -> int:
        return self.vertex_count()

    def __str__(self) -> str:
        with self._lock:
            return f"Graph(directed={self.directed}, vertices={len(self._graph)}, edges={self._edge_count})"

g = Graph(directed=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('Z')
g.add_vertex('X')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('Z', 'X')
print(g)

adj_A = g.get_adjacent_vertices('A')
print(adj_A)

adj_Z = g.get_adjacent_vertices('Z')
print(adj_Z)