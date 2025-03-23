import numpy as np

EQUATIONS = {
    "x^2 - 2": {
        "f": lambda x: x ** 2 - 2,
        "df": lambda x: 2 * x,
        "phi": lambda x: (x + 2 / x) / 2
    },
}

SYSTEMS = {
    "x^2 + y^2 = 1; x + y = 0": {
        "phi1": lambda x, y: np.sqrt(1 - y ** 2),
        "phi2": lambda x, y: -x
    }
}
