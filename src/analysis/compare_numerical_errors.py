import matplotlib.pyplot as plt
from src.errors.numerical_errors import *


# Compare numerical errors of 3 types of interpolation
def compare_numerical_errors():
    fig, ax = plt.subplots(dpi=120)
    ax.semilogy(CONST_NODES_COUNT_ARRAY, get_numerical_error(CONST_EVENLY_SPACED_NODES), 'o-',
                label=CONST_NUMERICAL_LABELS[CONST_EVENLY_SPACED_NODES])
    ax.semilogy(CONST_NODES_COUNT_ARRAY, get_numerical_error(CONST_OPTIMALLY_SPACED_NODES), 'o-',
                label=CONST_NUMERICAL_LABELS[CONST_OPTIMALLY_SPACED_NODES])
    ax.semilogy(CONST_NODES_COUNT_ARRAY, get_numerical_error(CONST_PIECEWISE_LINEAR_INTERPOLATION), 'o-',
                label=CONST_NUMERICAL_LABELS[CONST_PIECEWISE_LINEAR_INTERPOLATION])
    ax.set(xlabel='Число узлов', ylabel='Значение ошибки')
    ax.legend(loc='best')
    ax.grid()
    plt.show()


# compare_numerical_errors()
