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
    040-re-raise.BadYValue: Y is zerro!
    """

    if y == 0:
        raise BadYValue("Y is zerro!")

    return x / y


def main() -> None:
    pass

    # try:
    #     1 / 0
    # except Exception as e:
    #     print('exception', e)
    #     raise

    # try:
    #     1 / 0
    # except Exception as e:
    #     print('exception', e)
    #     raise BadYValue("Bad Y value") from e


if __name__ == "__main__":
    main()
