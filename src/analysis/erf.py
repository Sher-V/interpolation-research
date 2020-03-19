from src.errors.numerical_errors import *


# Error function
def erf():
    x = 2.
    number_of_nodes = [3, 5, 7, 9]
    for n in number_of_nodes:
        x_nodes = np.linspace(*CONST_ARG_RANGE, n)
        y_nodes = np.exp(-x_nodes ** 2)
        h = (x - (-x)) / n
        res = 0.5 * (interpolate_linearly(x_nodes[0], x_nodes, y_nodes) + interpolate_linearly(x_nodes[n - 1],
                                                                                               x_nodes, y_nodes))
        for i in range(1, n):
            res += interpolate_linearly((-2. + i * h), x_nodes, y_nodes)
        print("N={0}, erf(x)={1}".format(n, res * h / m.sqrt(m.pi)))

# erf()
