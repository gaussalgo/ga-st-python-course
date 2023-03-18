#!/usr/bin/env python3


import logging
import logging.config

import logging_tree
import yaml

logger = logging.getLogger()


def sample_fce(msg: str, divisor: int) -> None:
    """
    Sample function: just print `msg` to stdout and divide 1 by `divisor`.

    >>> sample_fce("message1", 1)
    message1
    >>> sample_fce("message2", 0)
    message2
    """

    logger.debug("sample debug")
    logger.info("sample info")
    logger.warning("sample warning")
    logger.error("sample error")
    logger.critical("sample critical")

    try:
        1 / divisor
    except ZeroDivisionError as e:
        logger.exception("sample exception: %s", e)

    print(msg)


def main() -> None:
    global logger

    logging_tree.printout()
    print("-" * 50)

    D = yaml.load(open("logging.yml"), Loader=yaml.FullLoader)
    D.setdefault("version", 1)
    D.setdefault("disable_existing_loggers", True)
    logging.config.dictConfig(D)

    logging_tree.printout()
    print("-" * 50)

    logger = logging.getLogger("test")
    sample_fce("test", 1)

    logger = logging.getLogger("production")
    sample_fce("production", 0)


if __name__ == "__main__":
    main()
