#!/usr/bin/env python3


from functools import wraps
from typing import Any, Callable


def dummy_decorator(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        print("Enter the inner() function")
        ret = func(*args, **kwargs)
        print("Leave the inner() function")
        return ret

    return inner


def james() -> str:
    """
    return James

    >>> james()
    Enter the james() function
    Leave the james() function
    'James'
    """
    print("Enter the james() function")
    print("Leave the james() function")
    return "James"


@dummy_decorator
def bond() -> str:
    """
    return Bond

    >>> bond()
    Enter the inner() function
    Enter the bond() function
    Leave the bond() function
    Leave the inner() function
    'Bond'
    """
    print("Enter the bond() function")
    print("Leave the bond() function")
    return "Bond"


def main() -> None:
    # manually
    obj = dummy_decorator(james)
    ret = obj()
    print("ret james:", ret)

    # another way
    dummy_decorator(james)()

    # with decorator
    print("ret bond:", bond())


if __name__ == "__main__":
    main()
