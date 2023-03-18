#!/usr/bin/env python3


import logging

logger = logging.getLogger()


def main() -> None:
    data: dict[str, str] = {"clientip": "192.168.0.1", "user": "plebz"}

    logger.setLevel(logging.DEBUG)

    FORMAT = "%(asctime)s %(message)s"
    # FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)

    logger.warning("sample warning", extra=data)


if __name__ == "__main__":
    main()
