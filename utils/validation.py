def validate_interval(a, b, f):
    if a >= b:
        return False, "Интервал задан неверно"
    if f(a) * f(b) > 0:
        return False, "Нет корня или несколько корней"
    return True, ""
