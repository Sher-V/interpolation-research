import matplotlib.pyplot as plt
from src.errors.analytical_errors import *
from src.errors.numerical_errors import *
import src.analysis.erf
import src.analysis.compare_numerical_errors


class Interpolation:
    x_nodes = None
    type = None
    fig, ax = plt.subplots(dpi=120)

    def __init__(self, color, numerical_label, analytical_label) -> None:
        self.color, self.numerical_label, self.analytical_label = color, numerical_label, analytical_label
        self.y_nodes = np.exp(-self.x_nodes ** 2)

    def draw_graphs(self):
        self.ax.plot(CONST_FUNC_X, CONST_FUNC_Y, color='red', label='$f(x)$')
        self.ax.plot(CONST_FUNC_X, self.polynomial_values, color='blue', label='$L(x)$')
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        self.ax.text(0.05, 0.95, "$N={}$".format(CONST_NODES_COUNT), transform=self.ax.transAxes, fontsize=14,
                     verticalalignment='top', bbox=props)
        self.ax.set(xlabel='$x$', ylabel='$y$')
        self.ax.grid()
        self.ax.legend(loc='best')
        plt.show()

    def draw_numerical_error(self):
        self.ax.semilogy(CONST_NODES_COUNT_ARRAY, get_numerical_error(self.type), 'o', color=self.color,
                         label=self.numerical_label)
        self.ax.set(xlabel='Число узлов', ylabel='Значение ошибки')
        self.ax.legend(loc='best')
        self.ax.grid()
        plt.show()

    def draw_analytical_error(self):
        self.ax.semilogy(CONST_NODES_COUNT_ARRAY, get_analytical_error(self.type), 'o',
                         color=self.color,
                         label=self.analytical_label)
        self.ax.set(xlabel='Число узлов', ylabel='Значение ошибки')
        self.ax.legend(loc='best')
        self.ax.grid()
        plt.show()

    def compare_errors(self):
        self.ax.semilogy(CONST_NODES_COUNT_ARRAY, get_numerical_error(self.type), 'o',
                         color='red',
                         label=self.numerical_label)
        self.ax.semilogy(CONST_NODES_COUNT_ARRAY, get_analytical_error(self.type), 'o',
                         color='blue',
                         label=self.analytical_label)
        self.ax.set(xlabel='Число узлов', ylabel='Значение ошибки')
        self.ax.legend(loc='best')
        self.ax.grid()
        plt.show()


class EvenlySpacedNodes(Interpolation):
    x_nodes = np.linspace(*CONST_ARG_RANGE, CONST_NODES_COUNT)
    type = CONST_EVENLY_SPACED_NODES

    def __init__(self, color='blue') -> None:
        super().__init__(color, numerical_label=CONST_NUMERICAL_LABELS[self.type],
                         analytical_label=CONST_ANALYTICAL_LABELS[self.type])
        self.polynomial_values = [L(x, self.x_nodes, self.y_nodes) for x in CONST_FUNC_X]


class OptimallySpacedNodes(Interpolation):
    x_nodes = np.array([get_chebyshev_node(i, CONST_NODES_COUNT) for i in range(CONST_NODES_COUNT)])
    type = CONST_OPTIMALLY_SPACED_NODES

    def __init__(self, color='blue') -> None:
        super().__init__(color, numerical_label=CONST_NUMERICAL_LABELS[self.type],
                         analytical_label=CONST_ANALYTICAL_LABELS[self.type])
        self.polynomial_values = [L(x, self.x_nodes, self.y_nodes) for x in CONST_FUNC_X]


class PiecewiseLinearInterpolation(Interpolation):
    x_nodes = np.linspace(*CONST_ARG_RANGE, CONST_NODES_COUNT)
    type = CONST_PIECEWISE_LINEAR_INTERPOLATION

    def __init__(self, color='blue') -> None:
        super().__init__(color, numerical_label=CONST_NUMERICAL_LABELS[self.type],
                         analytical_label=CONST_ANALYTICAL_LABELS[self.type])
        self.polynomial_values = [interpolate_linearly(x, self.x_nodes, self.y_nodes) for x in CONST_FUNC_X]


# Creating needed interpolation class
interpolation = PiecewiseLinearInterpolation()

# interpolation.draw_graphs()
# interpolation.draw_numerical_error()
# interpolation.draw_analytical_error()
# interpolation.compare_errors()
