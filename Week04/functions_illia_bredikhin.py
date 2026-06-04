import inspect


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

    :param x: First positional-only value.
    :param y: Second positional-only value.
    :param a: Exponent of x.
    :param b: Exponent of y.
    :param c: Divisor.
    :return: Result of equation.
    """
    return (x ** a + y ** b) / c


_counter = 0
_callers = {}


def fn_w_counter() -> (int, dict[str, int]):
    global _counter
    global _callers

    _counter += 1

    caller = inspect.stack()[1].filename
    caller = caller.split("/")[-1].replace(".py", "")

    _callers[caller] = _callers.get(caller, 0) + 1

    return _counter, _callers.copy()
