#!/usr/bin/env python3

import abc
import time


class Animal:
    def make_sound(self) -> None:
        pass

    @property
    def name(self) -> str:
        pass


class Animal_abc(abc.ABC):
    @abc.abstractmethod
    def make_sound(self) -> None:
        pass

    @abc.abstractproperty
    def name(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self) -> None:
        print("Woof!")

    @property
    def name(self) -> str:
        return "Dog"


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


if __name__ == "__main__":
    my_dog = Dog()
    my_cat = Cat()

    my_dog.make_sound()
    print(my_dog.name)

    time.sleep(5)

    my_cat.make_sound()
    print(my_cat.name)
