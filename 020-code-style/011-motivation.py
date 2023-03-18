#!/usr/bin/env python3

import random


def generate_keys(num):
    keys = [
        random.sample(range(index * 10, (index + 1) * 10), 10)
        for index in range(0, num)
    ]
    return keys


def main():
    keys = generate_keys(2)
    for number, key in enumerate(keys):
        print(f"key range {number} = {key}")


if __name__ == "__main__":
    main()
