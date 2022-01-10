from loguru import logger
from LinkAnalysis.HITS import directedGraph_HITS
from LinkAnalysis.PageRank import directedGraph_PageRank
from LinkAnalysis.SimRank import directedGraph_SimRank

from utils.GraphStruct import directedGraph
from utils.fileIO import read_txt_as_a_graph

if __name__ == "__main__":

    for i in range(5):
        graph_txt = read_txt_as_a_graph(f"./dataset/hw03/graph_{i + 1}.txt")

        # print(graph_txt)

        # result_auth, result_hubs = directedGraph_HITS(graph_txt)
        # print(f"Auth: {result_auth}")
        # print(f"Hubs: {result_hubs}")
        # print(graph_txt.get_vertex_mapper())

        # directedGraph_PageRank(graph_txt)
        directedGraph_SimRank(graph_txt)
