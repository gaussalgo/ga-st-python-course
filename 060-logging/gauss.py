import collections
import logging
from typing import Deque, Optional

if hasattr(logging, "_levelNames"):
    NAME2LEVEL = logging._levelNames
else:
    NAME2LEVEL = logging._nameToLevel


class MultiLineFormatter(logging.Formatter):
    def __init__(self, fmt: Optional[str], datefmt: Optional[str]) -> None:
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record: logging.LogRecord) -> str:
        # hack: http://stackoverflow.com/a/5879524/533618
        backup_exc_text = record.exc_text
        record.exc_text = None
        formatted = logging.Formatter.format(self, record)
        message = record.getMessage()
        if message == "":
            header = formatted
        else:
            header = formatted.split(record.message)[0]
        record.exc_text = backup_exc_text
        return header + ("\n" + header).join(
            it for it in record.getMessage().split("\n") if it
        )


class LevelFilter(logging.Filter):
    def __init__(self, levels: list[str]) -> None:
        self.levels = [NAME2LEVEL[it] for it in levels]

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelno in self.levels


class NotLevelFilter(logging.Filter):
    def __init__(self, levels: list[str]) -> None:
        self.levels = [NAME2LEVEL[it] for it in levels]

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelno not in self.levels


class RingMemoryHandler(logging.Handler):
    """In memory logging handler with a circular buffer"""

    def __init__(
        self,
        capacity: int = 1024,
        flushLevel: str = "ERROR",
        target: Optional[logging.Handler] = None,
    ) -> None:
        logging.Handler.__init__(self)
        self.capacity = capacity
        self.flushLevel = NAME2LEVEL[flushLevel]
        self.target = target
        self.buffer: Deque[logging.LogRecord]
        self.reset_buffer()

    def reset_buffer(self) -> None:
        self.buffer = collections.deque(maxlen=self.capacity)

    def shouldFlush(self, record: logging.LogRecord) -> bool:
        """
        Check for buffer full or a record at the flushLevel or higher.
        """
        return record.levelno >= self.flushLevel

    def setTarget(self, target: logging.Handler) -> None:
        """
        Set the target handler for this handler.
        """
        self.target = target

    def flush(self) -> None:
        pass

    def my_flush(self) -> None:
        """
        For a RingMemoryHandler, flushing means just sending the buffered
        records to the target, if there is one.
        """

        self.acquire()
        try:
            if self.target:
                for record in self.buffer:
                    self.target.handle(record)
                self.reset_buffer()
        finally:
            self.release()

    def close(self) -> None:
        pass

    def emit(self, record: logging.LogRecord) -> None:
        self.buffer.append(record)
        if self.shouldFlush(record):
            self.my_flush()
