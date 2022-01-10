import numpy as np
from loguru import logger

from utils.GraphStruct import directedGraph

def evaluate_converge_score_pgrank(
    pgrank_prev: np.ndarray,
    pgrank_curr: np.ndarray,
) -> float:
    return np.linalg.norm(pgrank_curr - pgrank_prev, ord=1)


def evaluate_PageRank_new_pgrank(
    graph: directedGraph,
    pgrank_old: np.ndarray,
    damping_factor: float,
) -> np.ndarray:

    # Get graph information
    vertex_count = graph.vertex_count()
    pgrank_new = pgrank_old.copy()

    # Update page rank vertex-wisely
    for i in range(vertex_count):

        in_nodes_idx = graph.get_in_neighbours_index(i, True)
        # print(f"In-ancestor of {i} -> {in_nodes_idx}")

        pgrank_sum = sum(
            pgrank_new[idx] / graph.out_degree(idx, True) for idx in in_nodes_idx

        )
        # print(f"Pgrank_sum of {i} -> {pgrank_sum:.2f}")
        # print(f"Random Jumping: {random_jumping}")

        pgrank_new[i] = damping_factor / vertex_count + (1 - damping_factor) * pgrank_sum

    return pgrank_new / sum(pgrank_new) # Don't forget to do normalization


def directedGraph_PageRank(
    input_graph: directedGraph,
    converge_threshold: float = 1e-3,
    damping_factor: float = 0.15,
    max_iter: int = 100
) -> np.ndarray:
    # Initialize - prepare page rank vector
    vertex_count = input_graph.vertex_count()
    pgrank_array = np.ones((vertex_count,)) / vertex_count
    converge_score = np.inf

    # Loop Until reach specific conditions
    iter_cnt = 1

    while iter_cnt <= max_iter:

        pgrank_array_new = evaluate_PageRank_new_pgrank(
            input_graph,
            pgrank_array,
            damping_factor,
        )

        converge_score_new = evaluate_converge_score_pgrank(
            pgrank_array, pgrank_array_new,
        )

        print(f"Iteration: {iter_cnt}, convergence score: {converge_score_new}")
        print(f"original pgrank-> {pgrank_array}")
        print(f"pgrank result -> {pgrank_array_new}")
        print("-------------------------------------")

        if converge_score_new <= converge_threshold:
            logger.debug(f"Converged after {iter_cnt} iterations, score: {converge_score_new:.2f}")
            break

        if converge_score_new > converge_score:
            logger.warning(f"Pagerank Algorithm has stopped at {iter_cnt}-th iterations due to expected divergence.")
            logger.warning(f"Will return old sequence, Score: from {converge_score:.2f} to {converge_score_new:.2f}")
            break

        # Replace original array for next iteration
        pgrank_array = pgrank_array_new
        converge_score = converge_score_new

        iter_cnt += 1

    return pgrank_array
