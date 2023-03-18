#!/usr/bin/env python3


import sys
import time
from functools import cache


@cache
def hard_work(string: str = "not deffined") -> str:
    """
    Sample function: just print `string` to stdout.

    >>> hard_work(string="message")
    really working on message...done
    'message'
    """
    sys.stdout.write(f"really working on {string}...")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write("done\n")
    return string


def main() -> None:
    print("task1 1st:", hard_work("task1"))
    print("task1 2nd:", hard_work("task1"))
    print("task2 1st:", hard_work("task2"))
    print("task2 2nd:", hard_work("task2"))


if __name__ == "__main__":
    main()
