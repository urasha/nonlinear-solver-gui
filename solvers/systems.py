from utils.config import SYSTEMS


def system_simple_iteration(
        system_name,
        x0,
        y0,
        eps = 1e-6,
        max_iter = 100,
        lambda_ = 0.7,
):
    phi1 = SYSTEMS[system_name]["phi1"]
    phi2 = SYSTEMS[system_name]["phi2"]

    errors = []
    x_prev, y_prev = x0, y0

    for iteration in range(max_iter):
        try:
            x_next = x_prev + lambda_ * (phi1(x_prev, y_prev) - x_prev)
            y_next = y_prev + lambda_ * (phi2(x_prev, y_prev) - y_prev)
        except ValueError as e:
            raise RuntimeError(f"Ошибка вычисления: {str(e)}")

        error_x = abs(x_next - x_prev)
        error_y = abs(y_next - y_prev)
        errors.append((error_x, error_y))

        if error_x < eps and error_y < eps:
            break

        x_prev, y_prev = x_next, y_next

    return (x_next, y_next), iteration + 1, errors
