def chord_method(f, a, b, eps, max_iter=1000):
    iterations = 0
    c = a
    while abs(b - a) > eps and iterations < max_iter:
        c = (a * f(b) - (b * f(a))) / (f(b) - f(a))
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return c, f(c), iterations


def newton_method(f, df, x0, eps, max_iter=1000):
    iterations = 0
    x = x0
    while abs(f(x)) > eps and iterations < max_iter:
        x = x - f(x) / df(x)
        iterations += 1
    return x, f(x), iterations


def simple_iteration_method(f, df, a, b, x0, eps, max_iter=1000):
    mx = max(abs(df(a)), abs(df(b)))
    lambda_param = 1 / mx

    phi = lambda x: x + lambda_param * f(x)

    phi_prime = lambda x: 1 + lambda_param * df(x)
    for x in [a, b]:
        if abs(phi_prime(x)) >= 1:
            raise ValueError("Условие сходимости не выполнено на интервале.")

    iterations = 0
    x_prev = x0
    while True:
        x_next = phi(x_prev)
        iterations += 1

        if abs(x_next - x_prev) < eps or iterations >= max_iter:
            break

        x_prev = x_next

    return x_next, f(x_next), iterations
