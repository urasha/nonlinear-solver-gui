import numpy as np

EQUATIONS = {
    "-1.8x³ - 2.94x² + 10.37x + 5.38": {
        "f": lambda x: -1.8 * x ** 3 - 2.94 * x ** 2 + 10.37 * x + 5.38,
        "df": lambda x: -5.4 * x ** 2 - 5.88 * x + 10.37,
    },

    "x³ - 4.5x² - 9.21x - 0.383": {
        "f": lambda x: x ** 3 - 4.5 * x ** 2 - 9.21 * x - 0.383,
        "df": lambda x: 3 * x ** 2 - 9 * x - 9.21,
    },

    "x³ + 4.81x² - 17.37x + 5.38": {
        "f": lambda x: x ** 3 + 4.81 * x ** 2 - 17.37 * x + 5.38,
        "df": lambda x: 3 * x ** 2 + 9.62 * x - 17.37,
    }
}

SYSTEMS = {
    "sin(x+y) = 1.5x - 0.1; x² + 2y² = 1": {
        "phi1": lambda x, y: (np.sin(x + y) + 0.1) / 1.5,
        "phi2": lambda x, y: np.sqrt((1 - x ** 2) / 2) * (1 if y >= 0 else -1)
    },

    "sin(x+0.5) - y = 1; cos(y-2) + x = 0": {
        "phi1": lambda x, y: -np.cos(y - 2),
        "phi2": lambda x, y: np.sin(x + 0.5) - 1
    },

    "sin(x+y) - 1.4x = 0; x² + y² = 1": {
        "phi1": lambda x, y: np.sin(x + y) / 1.4,
        "phi2": lambda x, y: np.sqrt(max(0, 1 - x ** 2)) * (1 if abs(y) < 1e-10 else np.sign(y))
    }
}
