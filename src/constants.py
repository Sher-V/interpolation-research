import numpy as np

CONST_EVENLY_SPACED_NODES = "EVENLY_SPACED_NODES"
CONST_OPTIMALLY_SPACED_NODES = "OPTIMALLY_SPACED_NODES"
CONST_PIECEWISE_LINEAR_INTERPOLATION = "PIECEWISE_LINEAR_INTERPOLATION"

CONST_ARG_RANGE = [-5, 5]
CONST_NODES_COUNT = 15
CONST_POINTS_COUNT = 200
CONST_MIN_NODES_COUNT = 4
CONST_MAX_NODES_COUNT = 20

CONST_FUNC_X = np.linspace(*CONST_ARG_RANGE, CONST_POINTS_COUNT)
CONST_FUNC_Y = np.exp(-CONST_FUNC_X ** 2)
CONST_NODES_COUNT_ARRAY = range(CONST_MIN_NODES_COUNT, CONST_MAX_NODES_COUNT + 1)

CONST_NUMERICAL_LABELS = {
    CONST_EVENLY_SPACED_NODES: "Численная погрешность при равномерном распределении",
    CONST_OPTIMALLY_SPACED_NODES: "Численная погрешность при чебышевском распределении",
    CONST_PIECEWISE_LINEAR_INTERPOLATION: "Численнная погрешность кусочно-линейной интерполяции"
}

CONST_ANALYTICAL_LABELS = {
    CONST_EVENLY_SPACED_NODES: "Аналитическая погрешность при равномерном распределении",
    CONST_OPTIMALLY_SPACED_NODES: "Аналитическая погрешность при чебышевском распределении",
    CONST_PIECEWISE_LINEAR_INTERPOLATION: "Аналитическая погрешность кусочно-линейной интерполяции"
}
