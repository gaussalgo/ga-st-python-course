#!/usr/bin/env python3

from hr_module.internaldb import hr_catalog


def print_personal_info(person_dict):
    print("============================")
    for key, value in person_dict.items():
        print(f"{key} = {value.upper()}")


def main():
    for person in hr_catalog:
        print_personal_info(dict(person))


if __name__ == "__main__":
    main()
