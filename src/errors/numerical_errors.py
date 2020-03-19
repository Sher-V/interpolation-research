from sympy import *
from src.constants import *
from src.utils import *


# Max distance
def count_distance(polynomial_values, func_y):
    max_distance = 0
    for i in range(CONST_POINTS_COUNT):
        if (abs(polynomial_values[i] - func_y[i])) > max_distance:
            max_distance = abs(polynomial_values[i] - func_y[i])
    return max_distance


def getNodesByType(t, nodes_count):
    switcher = {
        CONST_EVENLY_SPACED_NODES: np.linspace(*CONST_ARG_RANGE, nodes_count),
        CONST_OPTIMALLY_SPACED_NODES: np.array([get_chebyshev_node(i, nodes_count) for i in range(nodes_count)]),
        CONST_PIECEWISE_LINEAR_INTERPOLATION: np.linspace(*CONST_ARG_RANGE, nodes_count),
    }

    return switcher.get(t)


# Count numerical error
def get_numerical_error(t):
    distances = []
    for nodes_count in CONST_NODES_COUNT_ARRAY:
        x_nodes = getNodesByType(t, nodes_count)
        y_nodes = np.exp(-x_nodes ** 2)
        polynomial_values = [interpolate_by_type(t, x, x_nodes, y_nodes) for x in CONST_FUNC_X]
        distances.append(count_distance(polynomial_values, CONST_FUNC_Y))
    return distances
