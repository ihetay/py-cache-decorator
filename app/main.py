from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = dict()
    def wrapper(*args, **kwargs) -> Any:
        nonlocal storage
        if args not in storage:
            storage[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return storage[args]
    return wrapper