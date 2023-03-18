#!/usr/bin/env python3


import logging
from functools import cache
from typing import Any

logger = logging.getLogger()


@cache
def get_clinet_ip() -> str:
    """
    get client IP address as string

    >>> len(get_clinet_ip()) >= 7
    True
    """
    import socket

    return socket.gethostbyname(socket.gethostname())


orig_factory = logging.getLogRecordFactory()


def record_factory(*args: Any, **kwargs: Any) -> logging.LogRecord:
    record = orig_factory(*args, **kwargs)
    record.clientip = get_clinet_ip()
    return record


def main() -> None:
    logger.setLevel(logging.DEBUG)

    FORMAT = "%(asctime)s %(clientip)-15s %(message)s"
    logging.setLogRecordFactory(record_factory)
    logging.basicConfig(format=FORMAT)

    logger.warning("sample warning")


if __name__ == "__main__":
    main()
