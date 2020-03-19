from src.constants import *
import math as m


# Obtain the value of the i-th base Lagrange polynomial
def l_i(i, x, x_nodes):
    result = 1
    for nodeIndex in range(len(x_nodes)):
        if nodeIndex != i:
            result *= (x - x_nodes[nodeIndex]) / (x_nodes[i] - x_nodes[nodeIndex])
    return result


# Count the value of the Lagrange polynomial at the point x
def L(x, x_nodes, y_nodes):
    assert len(x_nodes) == len(y_nodes)
    result = 0
    for nodeIndex in range(len(x_nodes)):
        result += y_nodes[nodeIndex] * l_i(nodeIndex, x, x_nodes)
    return result


# Piecewise linear interpolation
def interpolate_linearly(x, x_nodes, y_nodes):
    assert len(x_nodes) == len(y_nodes)
    result = 0
    for i in range(len(y_nodes) - 1):
        if x_nodes[i] <= x <= x_nodes[i + 1]:
            result = y_nodes[i] + ((x - x_nodes[i]) * (y_nodes[i + 1] - y_nodes[i]) / (x_nodes[i + 1] - x_nodes[i]))
    return result


# Interpolate by type
def interpolate_by_type(t, x, x_nodes, y_nodes):
    switcher = {
        CONST_EVENLY_SPACED_NODES: L,
        CONST_OPTIMALLY_SPACED_NODES: L,
        CONST_PIECEWISE_LINEAR_INTERPOLATION: interpolate_linearly
    }
    return switcher[t](x, x_nodes, y_nodes)


# Get Chebyshev`s node by index
def get_chebyshev_node(i, n):
    a, b = CONST_ARG_RANGE
    x_opt = m.cos(m.pi / n * (0.5 + i))
    return ((b - a) * x_opt + a + b) / 2
