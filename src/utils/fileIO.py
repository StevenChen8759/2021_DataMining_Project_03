import os

from loguru import logger
from graphviz import Digraph

from utils.GraphStruct import directedGraph


def mkdir_conditional(dirname: str):

    if not os.path.isdir(dirname):
        os.mkdir(dirname)


def read_txt_as_a_graph(filename: str) -> directedGraph:

    with open(filename, "r") as graph_file:
        edges = [
            tuple(
                # Remove '\n' in edge text if exists, then convert to tuple
                (edge_text[:-1] if edge_text[-1] == '\n' else edge_text).split(",")
            )
            for edge_text in graph_file.readlines() # Read all lines as edges
        ]

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

    return directedGraph(
        vertexes,
        edges,
    )


def visualize_directed_graph_with_graphviz(graph: directedGraph, dataset_name: str, filename: str):

    mkdir_conditional(f"./output/{dataset_name}")
    mkdir_conditional(f"./output/{dataset_name}/gv_images")

    dot = Digraph(f'{filename}')

    for i, vertex in enumerate(graph.get_vertex_mapper()):
        dot.node(f"{i}", f"{vertex}")

    for src, dst in graph.get_edges():
        dot.edge(f'{src}', f'{dst}')

    dot.render(filename, f"./output/{dataset_name}/gv_images", format='jpg')
