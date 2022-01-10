from typing import List

from loguru import logger

from utils.GraphStruct import directedGraph
from utils.fileIO import mkdir_conditional, output_np_ndarray, read_txt_as_a_graph, visualize_directed_graph_with_graphviz
from LinkAnalysis.HITS import directedGraph_HITS
from LinkAnalysis.PageRank import directedGraph_PageRank

PAGERANK_DAMPING_FACTOR = 0.15
edges_to_append: List[List[tuple]] = [
    # Graph 1
    [
        ("1", "3"),
        ("1", "4"),
        ("1", "5"),
        ("2", "1"),
    ],
    # Graph 2
    [
        ("1", "3"),
        ("1", "4"),
        ("1", "5"),
        ("2", "1"),
        ("3", "1"),
        ("4", "1"),
    ],
    # Graph 3
    [
        ("1", "3"),
        ("1", "4"),
        ("3", "1"),
        ("4", "1"),
    ],
]


if __name__ == "__main__":

    logger.info("Initialize...")
    mkdir_conditional("./output")
    mkdir_conditional("./output/hw03")
    mkdir_conditional("./output/ibm_data")

#----------------------------------------------------------------------------------------------------

    logger.info("Read Graphs")
    hw03_graphs: List[directedGraph] = [
        read_txt_as_a_graph(f"./dataset/hw03/graph_{i + 1}.txt")
        for i in range(3)
    ]

#----------------------------------------------------------------------------------------------------

    for i, graph_test in enumerate(hw03_graphs):

        logger.info(f"Run Graph {i + 1} Testing")

        logger.debug("Evaluate original authority and hub by HITS algorithm...")
        original_auth, original_hubs = directedGraph_HITS(graph_test)

        logger.debug("Evaluate original pagerank by PageRank algorithm...")
        original_pgrank = directedGraph_PageRank(graph_test, damping_factor=PAGERANK_DAMPING_FACTOR)

        logger.debug(f"Original Value:\nAuthority:\n{original_auth}\nHubs:\n{original_hubs}\nPageRank:\n{original_pgrank}")

        logger.debug(f"Add edges in graph {i + 1}")
        graph_test.link_edge(
            edges_to_append[i]
        )

        logger.debug("Evaluate new authority and hub by HITS algorithm...")
        new_auth, new_hubs = directedGraph_HITS(graph_test)

        logger.debug("Evaluate pagerank by PageRank algorithm...")
        new_pgrank = directedGraph_PageRank(graph_test, damping_factor=PAGERANK_DAMPING_FACTOR)

        logger.debug(f"Updated Value:\nAuthority:\n{new_auth}\nHubs:\n{new_hubs}\nPageRank:\n{new_pgrank}")


        logger.log(
            "SUCCESS" if new_auth[0] > original_auth[0] else "ERROR",
            f"Update Graph {i + 1} to increase authority: {'Passed' if new_auth[0] > original_auth[0] else 'Failed'}"
        )

        logger.log(
            "SUCCESS" if new_hubs[0] > original_hubs[0] else "ERROR",
            f"Update Graph {i + 1} to increase hubs: {'Passed' if new_hubs[0] > original_hubs[0] else 'Failed'}"
        )

        logger.log(
            "SUCCESS" if new_pgrank[0] > original_pgrank[0] else "ERROR",
            f"Update Graph {i + 1} to increase page rank: {'Passed' if new_pgrank[0] > original_pgrank[0] else 'Failed'}"
        )

        logger.info(f"Output graph {i + 1} with edge added")
        visualize_directed_graph_with_graphviz(graph_test, "hw03", f"graph_{i + 1}_update_edges")
        print("****************************************************************************************************************************")
