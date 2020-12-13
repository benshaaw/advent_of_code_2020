#!/usr/bin/env python

import re
import os
import sys

import d1
import d2
import d3

if __name__ == "__main__":
    os.chdir(
        os.path.dirname(os.path.realpath(__file__))
    )
    if len(sys.argv) != 3:
        sys.exit("./aoc <<advent_day>> <<exercise_number>>")
    elif not all([ re.match(r"[0-9]+", arg) for arg in sys.argv[1:]]):
        sys.exit("advent_day and exercise_number must be numeric")
    if sys.argv[1] == "1":
        import d1 as d
    elif sys.argv[1] == "2":
        import d2 as d
    elif sys.argv[1] == "3":
        import d3 as d
    else:
        sys.exit("Invalid day")
        
    if sys.argv[2] == "1":
        d.exercise_1()
    elif sys.argv[2] == "2":
        d.exercise_2()
    else:
        sys.exit("Invalid exercise")
            
