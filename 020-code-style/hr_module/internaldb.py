import random

from typing import Optional, List

from .personlib import Person


def get_catalog() -> List[Optional[Person]]:
    if random.random() < 0.1:
        return [None]
    else:
        return [
            Person(name="Andy", city="Bratislava"),
            Person(name="Suzy", city="Brno"),
            Person(name="Michal", city="Praha"),
        ]


hr_catalog = get_catalog()
