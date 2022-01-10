import numpy as np
from loguru import logger
from LinkAnalysis.HITS import evaluate_converge_score

from utils.GraphStruct import directedGraph

def evaluate_converge_score_simrank(
    simrank_prev: np.ndarray,
    simrank_curr: np.ndarray,
) -> float:
    return np.linalg.norm(simrank_curr - simrank_prev, ord=1)


def evaluate_SimRank_new_simrank(
    graph: directedGraph,
    simrank_old: np.ndarray,
    decay_factor: float,
) -> np.ndarray:

    vertex_count = graph.vertex_count()
    simrank_new = simrank_old.copy()

    # Traverse each vertices-pair twice
    for i in range(vertex_count):
        for j in range(vertex_count):

            if i == j:
                continue

            in_neighbours_i = graph.get_in_neighbours_index(i, True)
            in_neighbours_j = graph.get_in_neighbours_index(j, True)

            if len(in_neighbours_i) == 0 or len(in_neighbours_j) == 0:
                simrank_new[i][j] = 0.0
                continue

            simrank_sum = sum(
                simrank_old[nb_i][nb_j]
                for nb_j in in_neighbours_j
                for nb_i in in_neighbours_i
            )

            simrank_new[i][j] = simrank_sum * decay_factor / (len(in_neighbours_i) * len(in_neighbours_j))

    return simrank_new


def directedGraph_SimRank(
    input_graph: directedGraph,
    decay_factor: float = 0.9,
    converge_threshold: float = 1e-3,
    max_iter = 10,
) -> np.ndarray:
    # Initialization
    vertex_count = input_graph.vertex_count()
    simrank_array = np.identity(vertex_count)
    converge_score = np.inf

    # Loop Until reach specific conditions
    iter_cnt = 1

    while iter_cnt <= max_iter:

        simrank_array_new = evaluate_SimRank_new_simrank(
            input_graph,
            simrank_array,
            decay_factor,
        )

        # TODO: Check if the process of convergence score evaluating is reasonable.
        converge_score_new = evaluate_converge_score_simrank(
            simrank_array,
            simrank_array_new,
        )

        print(f"Iteration: {iter_cnt}, convergence score: {converge_score_new}")
        print(f"original simrank -> \n{simrank_array}")
        print(f"simrank result -> \n{simrank_array_new}")
        print("-------------------------------------")

        if converge_score_new <= converge_threshold:
            logger.debug(f"Converged after {iter_cnt} iterations, score: {converge_score_new:.2f}")
            break

        if converge_score_new > converge_score:
            logger.warning(f"SimRank Algorithm has stopped at {iter_cnt}-th iterations due to expected divergence.")
            logger.warning(f"Will return old sequence, Score: from {converge_score:.2f} to {converge_score_new:.2f}")
            break

        # Replace original array for next iteration
        simrank_array = simrank_array_new
        converge_score = converge_score_new

        iter_cnt += 1

    return simrank_array
