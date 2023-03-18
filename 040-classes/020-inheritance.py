#!/usr/bin/env python3


class A:
    def __init__(self):
        self.a = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.a += 1


class C(A):
    def __init__(self):
        super().__init__()
        self.a += 2


class D(B, C):
    def __init__(self):
        super().__init__()
        self.a += 3


if __name__ == "__main__":
    my_d = D()
    print(my_d.a)
    print(D.mro())
