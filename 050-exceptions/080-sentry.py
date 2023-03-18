#!/usr/bin/env python3

import sentry_sdk


def main() -> None:
    sentry_sdk.init(
        "https://b2550c822e55435b9f8e1d42f9f079a3@sentry.gaussalgo.com/36",
        traces_sample_rate=1.0,
    )

    try:
        1 / 0
    except Exception as e:
        sentry_sdk.capture_exception(e)

    sentry_sdk.capture_message("Something went wrong")

    data: dict[str, int] = dict()

    # raise an exception
    assert data["key"]


if __name__ == "__main__":
    main()
