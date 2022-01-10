from loguru import logger
from utils.GraphStruct import directedGraph

from utils.fileIO import mkdir_conditional, read_txt_as_a_graph, visualize_directed_graph_with_graphviz

FILENAME = 'ibm-5000'

if __name__ == "__main__":

    # TODO: Make filename and pathname as command line arguments
    logger.info("Initialize...")
    mkdir_conditional("./output")

#------------------------------------------------------------------------------------------------
    logger.info("Adjustment and remove first column, then output preprocessed dataset...")
    with open(f'./dataset/ibm_data/{FILENAME}.txt', 'r') as ibm_data_reader:
        ibm_data_content = [
            edge[:-1].split()[1:]
            for edge in ibm_data_reader.readlines()
        ]

    logger.debug(f"{len(ibm_data_content)} Lines Processed")

    logger.debug("Writing preprocessed lines")
    with open(f'./dataset/ibm_data/{FILENAME}_preprocessed.txt', 'w') as ibm_data_writer:
        for line in ibm_data_content:
            ibm_data_writer.write(f"{','.join(line)}\n")
    logger.success("Write preprocessed file finished.")

#------------------------------------------------------------------------------------------------

    logger.info("Read IBM Graph")
    ibm_graph: directedGraph = read_txt_as_a_graph(f"./dataset/ibm_data/{FILENAME}_preprocessed.txt")

    logger.info("Visualize Graph with Graphviz")
    logger.warning("This step is a long-run task, you can use Ctrl-C to stop it.")
    visualize_directed_graph_with_graphviz(ibm_graph, "ibm_data", FILENAME)
