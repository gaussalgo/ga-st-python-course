#!/usr/bin/env python3


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    """
    just return hello world

    >>> hello()
    'Hello, World!'
    """

    return "Hello, World!"


@app.route("/test")
def status() -> str:
    """
    just return ok

    >>> status()
    'OK!'
    """

    return "OK!"


@app.route("/len/<message>")
def length(message: str) -> str:
    """
    count length of the `message`

    >>> length('test')
    'length: 4'
    """

    return f"length: {len(message)}"


def main() -> None:
    app.run(debug=True)


if __name__ == "__main__":
    main()
