from typing import List

from loguru import logger

from utils.GraphStruct import directedGraph
from utils.fileIO import mkdir_conditional, read_txt_as_a_graph, visualize_directed_graph_with_graphviz


if __name__ == "__main__":

    logger.info("Initialize...")
    mkdir_conditional("./output")

    logger.info("Read Graphs")
    hw03_graphs: List[directedGraph] = [
        read_txt_as_a_graph(f"./dataset/hw03/graph_{i + 1}.txt")
        for i in range(6)
    ]

    logger.info("Visualize Graph with Graphviz")
    logger.warning("This step is a long-run task, you can use Ctrl-C to stop it.")
    for i, graph in enumerate(hw03_graphs):
        logger.debug(f"Currently visualizing: graph_{i + 1}")
        visualize_directed_graph_with_graphviz(graph, "hw03", f"graph_{i + 1}")