#!/usr/bin/env python

import itertools

def get_input():
    with open("d1_input", "r") as f:
        raw = f.read()
        return [
            int(line)
            for line in list(filter(lambda x: x != "", raw.split("\n")))
        ]


def exercise_1():
    for x, y in set(itertools.combinations(get_input(), 2)):
        if x + y == 2020:
            print(x, y)
            print(x * y)


def exercise_2():
    for x, y, z in set(itertools.combinations(get_input(), 3)):
        if x + y + z == 2020:
            print(x, y, z)
            print(x * y * z)
