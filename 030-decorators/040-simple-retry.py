#!/usr/bin/env python3


from typing import Any, Callable


def retry(func: Callable) -> Callable:
    def inner(*args: Any, **kwargs: Any) -> Any:
        max: int = 10
        counter: int = 0

        while True:
            try:
                print(f"going to call {func}, {counter}")
                return func(*args, **kwargs)
            except Exception as e:
                counter += 1
                if counter >= max:
                    print(f"max {max} reached with {e}")
                    raise

    return inner


@retry
def divide(x: float, y: float) -> float:
    """
    divide `x` by `y`

    >>> divide(6, 3)
    going to call ..., 0
    2.0
    """
    return x / y


def divide_no_decore(x: float, y: float) -> float:
    """
    divide `x` by `y`

    >>> divide_no_decore(6, 3)
    2.0
    """

    return x / y


def main() -> None:
    print("1st", divide(1.0, 1.0))
    print("2nd", retry(divide_no_decore)(2.0, 1.0))
    print("3rd", divide(1.0, 0.0))


if __name__ == "__main__":
    main()
