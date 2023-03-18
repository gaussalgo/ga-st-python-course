#!/usr/bin/env python3


import datetime
import logging
import sys
import time

import gauss
import graypy

logger = logging.getLogger()


class MyFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return not ("test" in record.getMessage())


def main() -> None:
    logger.handlers.clear()

    fmt = "%(asctime)s.%(msecs).03d %(process)+5s %(levelname)-8s %(filename)s:%(lineno)d:%(funcName)s(): %(message)s"  # noqa: E501
    sh = logging.StreamHandler(sys.stderr)
    sh.setFormatter(logging.Formatter(fmt, "%Y-%m-%d %H:%M:%S"))

    handler_graylog = graypy.GELFHTTPHandler("graylog.gaussalgo.com", 12201)

    handler_ring_memory = gauss.RingMemoryHandler(
        capacity=100, flushLevel="ERROR", target=handler_graylog
    )

    sh.addFilter(MyFilter())

    logger.addHandler(handler_ring_memory)
    logger.addHandler(sh)

    logger.setLevel(logging.DEBUG)
    # logger.setLevel(logging.INFO)
    # logger.setLevel(logging.WARNING)

    logger.info("this is the test info message @ {}".format(datetime.datetime.now()))

    for _ in range(5):
        logger.debug("this is the debug message @ {}".format(datetime.datetime.now()))
        logger.info("this is the info message @ {}".format(datetime.datetime.now()))
        logger.warning(
            "this is the warning message @ {}".format(datetime.datetime.now())
        )
        time.sleep(0.1)

    logger.error("this is the error message @ {}".format(datetime.datetime.now()))


if __name__ == "__main__":
    main()
