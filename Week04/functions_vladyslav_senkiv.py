custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(
    x: int = 0,
    y: int = 0,
    /,
    a: int = 1,
    b: int = 1,
    *,
    c: int = 1
) -> float:
    """
    Calculates custom equation.

    :param x: first number
    :param y: second number
    :param a: coefficient for x
    :param b: coefficient for y
    :param c: divisor
    :return: result of equation
    """

    values = [x, y, a, b, c]

    for value in values:
        if not isinstance(value, int):
            raise TypeError("value must be int")

    return (x * a + y * b) / c


counter = 0


def fn_w_counter() -> (int, dict[str, int]):
    global counter

    counter += 1

    return counter, {__name__: counter}
