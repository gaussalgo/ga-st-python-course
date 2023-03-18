#!/usr/bin/env python3


import sys
from types import TracebackType
from typing import Any, Optional, Type


def info(
    type: Type[BaseException], value: BaseException, tb: Optional[TracebackType]
) -> Any:
    if hasattr(sys, "ps1") or not sys.stderr.isatty():
        # we are in interactive mode or we don't have a tty-like
        # device, so we call the default hook
        sys.__excepthook__(type, value, tb)
    else:
        import traceback

        import ipdb

        # we are NOT in interactive mode, print the exception...
        traceback.print_exception(type, value, tb)
        print
        # ...then start the debugger in post-mortem mode.
        ipdb.post_mortem(tb)  # more "modern"


if sys.excepthook == sys.__excepthook__:
    # if someone already patched excepthook, let them win
    sys.excepthook = info


def main() -> None:
    print(1 / 1)


if __name__ == "__main__":
    main()
