#!/usr/bin/env python3


import logging

import graypy

logger = logging.getLogger()


def main() -> None:
    logger.setLevel(logging.INFO)

    handler = graypy.GELFHTTPHandler("graylog.gaussalgo.com", 12201)
    logger.addHandler(handler)

    logger.info("Hello Graylog!")


if __name__ == "__main__":
    main()
