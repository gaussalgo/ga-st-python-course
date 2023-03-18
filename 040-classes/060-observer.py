#!/usr/bin/env python3

import random
import time

from abc import ABC, abstractmethod
from typing import Dict, TypeVar


class AbstractManager(ABC):
    @abstractmethod
    def update(self, result: int) -> None:
        pass


class AbstractObservable(ABC):
    @abstractmethod
    def attach(self, observer: AbstractManager) -> None:
        pass

    @abstractmethod
    def notify(self, result: int) -> None:
        pass


class Observable(AbstractObservable):
    pass


class Worker(Observable):
    def _think(self):
        time.sleep(3)

    def _work(self) -> int:
        return random.randint(0, 100)

    def work(self, rounds: int = 4) -> None:
        round = 0
        while round < rounds:
            self._think()
            result = self._work()
            self.notify(result)
            round += 1


class Manager(AbstractManager):
    def update(self, result: int) -> None:
        if result < 20:
            print(f"Manager: {result}? You are fired!")
        else:
            print("Manager: Ok, next please.")


class Director(AbstractManager):
    def update(self, result: int) -> None:
        if result > 70:
            print("Director: Great job!")
        else:
            print("Director: Meh.")


if __name__ == "__main__":
    worker = Worker()

    manager = Manager()
    director = Director()

    worker.attach(manager)
    worker.attach(director)

    worker.work()
