#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    surname: str
    age: int
    occupation: str = "unemployed"


if __name__ == "__main__":
    peter1 = Person("Peter", "Gray", 40)
    peter2 = Person("Peter", "Gray", 40)

    print(f"Is peter1 equal to peter2: {peter1 == peter2}")
