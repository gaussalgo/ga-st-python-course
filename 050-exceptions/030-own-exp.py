#!/usr/bin/env python3


class BadYValue(Exception):
    pass


def divide(x: float, y: float) -> float:
    """
    divide `x` by `y`

    >>> divide(6, 3)
    2.0
    >>> divide(6, 0)
    Traceback (most recent call last):
    ...
    030-own-exp.BadYValue: Y is zerro!
    """

    if y == 0:
        raise BadYValue("Y is zerro!")

    return x / y


def main() -> None:
    try:
        divide(x=1, y=0)
    except BadYValue as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
