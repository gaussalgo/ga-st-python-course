#!/usr/bin/env python3


import random
import time
from functools import wraps
from typing import Any, Callable


def timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        res = func(*args, **kwargs)
        print("Function took " + str(time.time() - start) + " seconds to run")
        return res

    return wrapper


@timer
def my_function(n: float) -> float:
    """
    return random number [0..1] after `n` seconds.

    >>> random.seed(0)
    >>> my_function(0)
    Function took ... seconds to run
    0.8444218515250481
    """

    time.sleep(n)
    return random.random()


def main() -> None:
    random.seed()

    resp = my_function(3)
    print("output:", resp)

    # help(my_function)


if __name__ == "__main__":
    main()
