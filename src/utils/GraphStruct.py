from typing import Any, List, Tuple

import numpy as np

class directedGraph(object):

    def __init__(
        self,
        vertex_list: List[Any] = [],
        edge_list: List[Tuple[Any, Any]] = [],
    ) -> "directedGraph":
        vertex_count = len(vertex_list)
        self.__adjmat = np.zeros((vertex_count, vertex_count), dtype=int)
        self.vertex_mapper = vertex_list
        self.link_edge(edge_list)

    def __repr__(self) -> str:
        return str(self.__adjmat)

    # def add_vertex(self, vertex_count: int = 1) -> Tuple[int, int]:
    #     self.__adjmat = np.pad(self.__adjmat, ((0, vertex_count), (0, vertex_count)), mode="constant", constant_values=0)

    def link_edge(self, edge_list: List[Tuple[Any, Any]]) -> None:
        for src, dst in edge_list:
            self.__adjmat[
                self.vertex_mapper.index(src),
                self.vertex_mapper.index(dst),
            ] = 1

    def in_degree(self, vertex: Any, byindex=False) -> int:
        return np.count_nonzero(self.__adjmat, axis=0)[  # Axis 0: row
            self.vertex_mapper.index(vertex) if not byindex else vertex
        ]

    def out_degree(self, vertex: Any, byindex=False) -> int:
        return np.count_nonzero(self.__adjmat, axis=1)[  # Axis 1: column
            self.vertex_mapper.index(vertex) if not byindex else vertex
        ]

    def vertex_count(self) -> int:
        return self.__adjmat.shape[0]

    def edge_count(self) -> int:
        return np.count_nonzero(self.__adjmat)

    def get_in_neighbours_index(self, vertex: Any, byindex=False) -> List[Any]:
        return np.where(self.__adjmat.T[
                self.vertex_mapper.index(vertex) if not byindex else vertex
            ] == 1
        )[0]

    def get_adjancy_matrix(self) -> np.ndarray:
        return self.__adjmat

    def get_vertex_mapper(self) -> List[Any]:
        return self.vertex_mapper

    def get_edges(self) -> List[Tuple[int, int]]:
        source, destination = np.where(self.__adjmat == 1)
        return [
            (src, dst) for src, dst in zip(source, destination)
        ]
