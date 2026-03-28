import inspect

# 1. custom_power
custom_power = lambda x=0, /, e=1: x ** e

# 2. custom_equation
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the custom equation (x**a + y**b) / c.

    :param x: The first base value (positional-only).
    :param y: The second base value (positional-only).
    :param a: Exponent for x (positional or keyword).
    :param b: Exponent for y (positional or keyword).
    :param c: Divisor (keyword-only).
    :return: The result of the equation as a float.
    :rtype: float
    """
    return float((x ** a + y ** b) / c)

# 3. fn_w_counter
def fn_w_counter() -> tuple[int, dict[str, int]]:
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.callers = {}
    
    caller_frame = inspect.stack()[1]
    caller_name = caller_frame.frame.f_globals.get('__name__', 'unknown')
    fn_w_counter.total_calls += 1
    fn_w_counter.callers[caller_name] = fn_w_counter.callers.get(caller_name, 0) + 1
    
    return fn_w_counter.total_calls, fn_w_counter.callers
