#!/usr/bin/env python3


import logging
import sys
from typing import Optional

SECRETS: list[str] = ["heslo123", "heslo456"]
logger = logging.getLogger()


class RemoveSecrets(logging.Formatter):
    def __init__(self, fmt: Optional[str], datefmt: Optional[str]) -> None:
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record: logging.LogRecord) -> str:
        output = logging.Formatter.format(self, record)
        for secret in SECRETS:
            output = output.replace(secret, "X" * len(secret))
        return output


def main() -> None:
    logger.handlers.clear()

    fmt = "%(asctime)s.%(msecs).03d %(process)+5s %(levelname)-8s %(filename)s:%(lineno)d:%(funcName)s(): %(message)s"  # noqa: E501
    sh = logging.StreamHandler(sys.stderr)
    sh.setFormatter(RemoveSecrets(fmt, "%Y-%m-%d %H:%M:%S"))
    logger.addHandler(sh)

    logger.setLevel(logging.INFO)

    logger.info("this is the hesloABC with info message")
    logger.info("this is the heslo123 with info message")
    logger.info("this is the heslo456 with info message")


if __name__ == "__main__":
    main()
