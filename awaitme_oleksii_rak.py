import inspect
from functools import wraps

def awaitme(func):

    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if inspect.isawaitable(result):
            return await result
        return result

    return wrapper
