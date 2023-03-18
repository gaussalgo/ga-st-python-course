#!/usr/bin/env python3


def f_inner(key: str) -> str:
    """
    returns value for `key` from `data`

    >>> f_inner("key1")
    'value1'
    """
    data: dict[str, str] = {"key1": "value1"}
    return data[key]


def f_middle(key: str) -> str:
    """
    call `f_inner`

    >>> f_middle("key1")
    'value1'
    """
    return f_inner(key)


def f_outter(key: str) -> str:
    """
    call `f_middle`

    >>> f_outter("key1")
    'value1'
    """
    return f_middle(key)


def main() -> None:
    print("value:", f_outter("key2"))


if __name__ == "__main__":
    main()
