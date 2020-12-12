#!/usr/bin/env python

import re
import os
import sys

import d1
import d2

if __name__ == "__main__":
    os.chdir(
        os.path.dirname(os.path.realpath(__file__))
    )
    if len(sys.argv) != 3:
        sys.exit("./aoc <<advent_day>> <<exercise_number>>")
    elif not all([ re.match(r"[0-9]+", arg) for arg in sys.argv[1:]]):
        sys.exit("advent_day and exercise_number must be numeric")
    else:
        try:
            {
                "1": {
                    "1": d1.exercise_1,
                    "2": d1.exercise_2,
                },
                "2": {
                    "1": d2.exercise_1,
                    "2": d2.exercise_2,
                },
            }.get(
                sys.argv[1],
            ).get(
                sys.argv[2],
            )()
        except AttributeError:
            sys.exit("Invalid advent_day or exercise_number")
