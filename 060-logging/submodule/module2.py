import logging

logger = logging.getLogger(__name__)


def fce2(string: str = "not deffined") -> None:
    """
    Sample function: just print `string` to stdout.

    >>> fce2(string="message")
    fce2: message
    """

    logger.debug("fce2: this is debug, argument is %s", string)
    logger.info("fce2: this is info, argument is %s", string)
    logger.warning("fce2: this is warning, argument is %s", string)
    logger.error("fce2: this is error, argument is %s", string)
    print("fce2:", string)
