#!/usr/bin/python3

from ..components.core import f


def func(x):
    return x + 1


def test_answer():
    print("was here00")
    f()
    print("was here01")
    assert func(3) == 5

