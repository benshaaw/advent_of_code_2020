#!/usr/bin/env python3

import sys

def get_input():
    with open("2_input", "r") as f:
        raw = f.read()
        print(list(map(lambda x: x.strip(), raw.split("\n"))))
        return [
            {
                "lower": int(line[0].split("-")[0]),
                "higher": int(line[0].split("-")[1]),
                "character": line[1].split(":")[0],
                "password": line[2],
            } for line in list(
                map(
                    lambda x: x.strip().split(" "),
                    list(filter(
                        lambda x: x != "",
                        raw.split("\n")
                    )),
                )
            )
        ]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need exercise number")
    else:
        {
            "1": exercise_1,
            "2": exercise_2,
        }.get(sys.argv[1], exercise_1)(get_input())

