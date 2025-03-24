def system_simple_iteration(phi1, phi2, x0, y0, eps, max_iter=1000):
    x_prev, y_prev = x0, y0
    iterations = 0
    errors = []

    while True:
        x_next = phi1(x_prev, y_prev)
        y_next = phi2(x_prev, y_prev)
        errors.append((abs(x_next - x_prev), abs(y_next - y_prev)))
        iterations += 1

        if (errors[-1][0] < eps and errors[-1][1] < eps) or iterations >= max_iter:
            break

        x_prev, y_prev = x_next, y_next

    return (x_next, y_next), iterations, errors
