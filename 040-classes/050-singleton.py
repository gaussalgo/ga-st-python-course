#!/usr/bin/env python3


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonType):
    def log(self, msg: str) -> None:
        print(f"{id(self)}: {msg}")


if __name__ == "__main__":
    logger1 = Logger()
    logger1.log("What a lovely day today!")

    logger2 = Logger()
    logger2.log("Yes, it is a beautiful day today!")
