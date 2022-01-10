from typing import List

from loguru import logger

from utils.GraphStruct import directedGraph
from utils.fileIO import mkdir_conditional, output_np_ndarray, read_txt_as_a_graph
from LinkAnalysis.HITS import directedGraph_HITS
from LinkAnalysis.PageRank import directedGraph_PageRank
from LinkAnalysis.SimRank import directedGraph_SimRank

PAGERANK_DAMPING_FACTOR = 0.15
SIMRANK_DECAY_FACTOR = 0.9

if __name__ == "__main__":

    logger.info("Initialize...")
    mkdir_conditional("./output")
    mkdir_conditional("./output/hw03")
    mkdir_conditional("./output/ibm_data")

#----------------------------------------------------------------------------------------------------

    logger.info("Read Graphs")
    hw03_graphs: List[directedGraph] = [
        read_txt_as_a_graph(f"./dataset/hw03/graph_{i + 1}.txt")
        for i in range(6)
    ]
    ibm_graph: directedGraph = read_txt_as_a_graph(f"./dataset/ibm_data/ibm-5000_preprocessed.txt")

#----------------------------------------------------------------------------------------------------

    logger.info("Run hw03 dataset")
    for i, graph in enumerate(hw03_graphs):
        logger.info(f"Graph {i + 1} - HITS")
        result_auth, result_hubs = directedGraph_HITS(graph)
        logger.debug(f'\nAuthority:\n{result_auth}\nHubs:\n{result_hubs}')
        output_np_ndarray(result_auth, f"./output/hw03/graph_{i + 1}_HITS_authority.txt")
        output_np_ndarray(result_hubs, f"./output/hw03/graph_{i + 1}_HITS_hub.txt")

        logger.info(f"Graph {i + 1} - PageRank, damping factor: {PAGERANK_DAMPING_FACTOR}")
        result_pgrank = directedGraph_PageRank(graph, damping_factor=PAGERANK_DAMPING_FACTOR)
        output_np_ndarray(result_pgrank, f"./output/hw03/graph_{i + 1}_PageRank.txt")
        logger.debug(f'\nPageRank:\n{result_pgrank}')

        logger.info(f"Graph {i + 1} - SimRank, decay factor: {SIMRANK_DECAY_FACTOR}")
        result_simrank = directedGraph_SimRank(graph, decay_factor=SIMRANK_DECAY_FACTOR)
        logger.debug(f'\nSimRank:\n{result_simrank}')
        output_np_ndarray(result_simrank, f"./output/hw03/graph_{i + 1}_SimRank.txt")


#----------------------------------------------------------------------------------------------------

    logger.info(f"Run IBM dataset - HITS")
    result_auth, result_hubs = directedGraph_HITS(ibm_graph)
    logger.debug(f'\nAuthority:\n{result_auth}\nHubs:\n{result_hubs}')
    output_np_ndarray(result_auth, "./output/ibm_data/graph_ibm-5000_HITS_authority.txt")
    output_np_ndarray(result_hubs, "./output/ibm_data/graph_ibm-5000_HITS_hub.txt")

    logger.info(f"Run IBM dataset - PageRank, damping factor: {PAGERANK_DAMPING_FACTOR}")
    result_pgrank = directedGraph_PageRank(ibm_graph, damping_factor=PAGERANK_DAMPING_FACTOR)
    logger.debug(f'\nPageRank:\n{result_pgrank}')
    output_np_ndarray(result_pgrank, f"./output/ibm_data/graph_ibm-5000_PageRank.txt")

    logger.info(f"Run IBM dataset - SimRank, decay factor: {SIMRANK_DECAY_FACTOR}")
    result_simrank = directedGraph_SimRank(ibm_graph, decay_factor=SIMRANK_DECAY_FACTOR)
    logger.debug(f'\nSimRank:\n{result_simrank}')
    output_np_ndarray(result_simrank, f"./output/ibm_data/graph_ibm-5000_SimRank.txt")

    logger.success("End of main script...")
