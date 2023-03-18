#!/usr/bin/env python3


import logging
import sys

import logging_tree
import requests
from submodule.module1 import fce1
from submodule.module2 import fce2

logger = logging.getLogger()


def main() -> None:
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler(sys.stdout)
    fmt = "%(asctime)s.%(msecs).03d %(process)+5s %(levelname)-8s %(filename)s:%(lineno)d:%(funcName)s(): %(message)s"  # noqa: E501
    sh.setFormatter(logging.Formatter(fmt, "%Y-%m-%d %H:%M:%S"))
    logger.handlers.clear()
    logger.addHandler(sh)

    logging_tree.printout()

    fce1("1st")
    fce2("1st")

    l1 = logging.getLogger("submodule.module1")
    l1.setLevel(logging.INFO)

    logging_tree.printout()

    fce1("2nd")
    fce2("2nd")

    logging_tree.printout()

    print(requests.get("https://httpbin.org/status/200"))

    l2 = logging.getLogger("urllib3")
    l2.propagate = False

    logging_tree.printout()

    print(requests.get("https://httpbin.org/status/202"))


if __name__ == "__main__":
    main()
