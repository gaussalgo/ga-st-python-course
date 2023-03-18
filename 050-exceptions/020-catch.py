#!/usr/bin/env python3


from typing import Optional


def get_value(key: str) -> str:
    """
    returs value for `key` from `data`

    >>> get_value("key1")
    'value1'
    """
    data: dict[str, str] = {"key1": "value1"}
    # 1 / 0
    return data[key]


def main() -> None:
    ret: Optional[str] = None

    try:
        # some code
        ret = get_value("key1")
    except KeyError:
        print("bad key")
    except Exception as e:
        print("something bad happend:", e)
    else:
        # execute if no exception
        print("no pain")
    finally:
        # always executed
        if ret is None:
            ret = "default"

    print(ret)


if __name__ == "__main__":
    main()
