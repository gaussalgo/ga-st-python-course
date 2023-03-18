#!/usr/bin/env python3


def get_value(key: str) -> str:
    """
    returs value for `key` from `data`

    >>> get_value("key1")
    'value1'
    """
    data: dict[str, str] = {"key1": "value1"}
    return data[key]


def divide(x: float, y: float) -> float:
    """
    divide `x` by `y`

    >>> divide(6, 3)
    2.0
    """
    return x / y


def main() -> None:
    get_value("key1")
    divide(1, 1)


if __name__ == "__main__":
    main()
