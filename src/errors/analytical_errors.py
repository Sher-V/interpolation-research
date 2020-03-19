from sympy import *
from src.constants import *


def count_evenly_spaced_nodes_error(nodes_count):
    x = symbols('x')
    f = exp(-x ** 2)
    f_prime = lambdify(x, f.diff(x, nodes_count))
    max_f_prime = 0
    max_prod = 0
    x_nodes = np.linspace(*CONST_ARG_RANGE, nodes_count)
    for x in CONST_FUNC_X:
        if f_prime(x) > max_f_prime:
            max_f_prime = f_prime(x)
        temp_prod = 1
        for x_node in x_nodes:
            temp_prod *= abs(x - x_node)
        if temp_prod > max_prod:
            max_prod = temp_prod
    return max_f_prime * max_prod / factorial(nodes_count)


# Count analytical error with optimally spaced nodes
def count_optimally_spaced_nodes_error(nodes_count):
    a, b = CONST_ARG_RANGE
    x = symbols('x')
    f = exp(-x ** 2)
    f_prime = lambdify(x, f.diff(x, nodes_count))
    max_f_prime = 0
    for x in CONST_FUNC_X:
        if abs(f_prime(x)) > max_f_prime:
            max_f_prime = abs(f_prime(x))
    return max_f_prime * ((b - a) / 2) ** nodes_count / (2 ** (nodes_count - 1) * factorial(nodes_count))


# Count analytical error in linear interpolation`s case
def count_linear_interpolation_error(nodes_count):
    a, b = CONST_ARG_RANGE
    return ((b - a) * (b - a)) / ((nodes_count - 1) * (nodes_count - 1) * 4)


# Count analytical error by type
def count_analytical_error(t, nodes_count):
    dispatch = {
        CONST_EVENLY_SPACED_NODES: count_evenly_spaced_nodes_error,
        CONST_OPTIMALLY_SPACED_NODES: count_optimally_spaced_nodes_error,
        CONST_PIECEWISE_LINEAR_INTERPOLATION: count_linear_interpolation_error
    }
    return dispatch[t](nodes_count)


# Count analytical error
def get_analytical_error(t):
    return [count_analytical_error(t, nodes_count) for nodes_count in CONST_NODES_COUNT_ARRAY]