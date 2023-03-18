#!/usr/bin/env python3


import os
import sys

DEBUG = os.environ.get("DEBUG", False)

if DEBUG:
    from IPython.core import ultratb

    sys.excepthook = ultratb.FormattedTB(  # type: ignore
        mode="Verbose", color_scheme="Linux", call_pdb=True, ostream=sys.__stdout__
    )


def main() -> None:
    print(1 / 1)


if __name__ == "__main__":
    main()
