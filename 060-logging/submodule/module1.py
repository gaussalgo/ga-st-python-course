import logging

logger = logging.getLogger(__name__)


def fce1(string: str = "not deffined") -> None:
    """
    Sample function: just print `string` to stdout.

    >>> fce1(string="message")
    fce1: message
    """

    logger.debug("fce1: this is debug, argument is %s", string)
    logger.info("fce1: this is info, argument is %s", string)
    logger.warning("fce1: this is warning, argument is %s", string)
    logger.error("fce1: this is error, argument is %s", string)
    print("fce1:", string)
