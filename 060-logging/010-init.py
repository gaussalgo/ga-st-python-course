#!/usr/bin/env python3


import logging

logger = logging.getLogger()


def main() -> None:
    logger.debug("sample debug")
    logger.info("sample info")
    logger.warning("sample warning")
    logger.error("sample error")
    logger.critical("sample critical")

    try:
        1 / 0
    except ZeroDivisionError as e:
        logger.exception("sample exception: %s", e)


if __name__ == "__main__":
    main()
