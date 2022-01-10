from typing import Tuple
import numpy as np
from loguru import logger

from utils.GraphStruct import directedGraph


def evaluate_converge_score(
    auth_prev: np.ndarray,
    auth_curr: np.ndarray,
    hubs_prev: np.ndarray,
    hubs_curr: np.ndarray,
) -> float:
    return np.linalg.norm(auth_curr - auth_prev) + np.linalg.norm(hubs_curr - hubs_prev)


def evaluate_HITS_new_auth_and_hubs(
    graph: directedGraph,
    auth_old: np.ndarray,
    hubs_old: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:

    # Get graph information
    graph_adjmat = graph.get_adjancy_matrix()

    # Evaluate new hubs matrix by multiplication
    auth_new = np.matmul(hubs_old, graph_adjmat)
    hubs_new = np.matmul(graph_adjmat, auth_old)

    # Do normalization, then return
    return (auth_new / np.sum(auth_new)), (hubs_new / np.sum(hubs_new))



def directedGraph_HITS(
    input_graph: directedGraph,
    converge_threshold: float = 1e-6,
    max_iter: int = 100,
) -> Tuple[np.ndarray, np.ndarray]:
    # Initialize - prepare auth and hub vector
    vertex_count = input_graph.vertex_count()
    auth_array = np.ones((vertex_count,))
    hubs_array = np.ones((vertex_count,))
    converge_score = np.inf

    # Loop Until reach specific conditions
    iter_cnt = 1

    while iter_cnt <= max_iter:
        auth_array_new, hubs_array_new = evaluate_HITS_new_auth_and_hubs(
            input_graph,
            auth_array,
            hubs_array,
        )

        converge_score_new = evaluate_converge_score(
            auth_array, auth_array_new,
            hubs_array, hubs_array_new
        )

        print(auth_array_new)
        print(hubs_array_new)
        print(f"[{iter_cnt}] -> {converge_score_new}")

        if converge_score_new <= converge_threshold:
            logger.debug(f"Converged after {iter_cnt} iterations, score: {converge_score_new:.2f}")
            break

        if converge_score_new > converge_score:
            logger.warning(f"HITS Algorithm has stopped at {iter_cnt}-th iterations due to expected divergence.")
            logger.warning(f"Will return old sequence, Score: from {converge_score:.2f} to {converge_score_new:.2f}")
            break

        # Replace original array for next iteration
        auth_array = auth_array_new
        hubs_array = hubs_array_new
        converge_score = converge_score_new

        iter_cnt += 1
        # print("--------------------------")

    return auth_array, hubs_array
