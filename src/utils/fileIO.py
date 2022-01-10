from loguru import logger

from utils.GraphStruct import directedGraph


def read_txt_as_a_graph(filename: str) -> directedGraph:

    with open(filename, "r") as graph_file:
        edges = [
            tuple(
                # Remove '\n' in edge text if exists, then convert to tuple
                (edge_text[:-1] if edge_text[-1] == '\n' else edge_text).split(",")
            )
            for edge_text in graph_file.readlines() # Read all lines as edges
        ]

    # print(edges)

    vertexes = sorted(  # Sort items in dictionary order
        list(           # Get list from set for uniqueness of elements
            set(        # Filter duplicated items using set structure
                [
                    edge[i] for i in [0, 1]     # Traverse src and dest of edge
                    for edge in edges           # Traverse each edges
                ]
            )
        )
    )

    # edges_for_graph = [
    #     (
    #         vertexes.index(edge[0]),
    #         vertexes.index(edge[1]),
    #     )
    #     for edge in edges
    # ]

    return directedGraph(
        vertexes,
        edges,
    )
