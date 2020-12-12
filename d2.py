#!/usr/bin/env python3

def get_input():
    with open("d2_input", "r") as f:
        raw = f.read()
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


def exercise_1():
    def matches_criteria(d):
        return d["lower"] <= d["password"].count(d["character"]) <= d["higher"]

    print(len(list(filter(
        matches_criteria,
        get_input()
    ))))


def exercise_2():
    def matches_criteria(d):
       if len(d["password"]) < d["higher"]:
           return d["password"][d["lower"] - 1] == d["character"]
       else:
           return (
               bool(d["password"][d["lower"] - 1] == d["character"]) ^
               bool(d["password"][d["higher"] - 1] == d["character"])
           )

    print(len(list(filter(
        matches_criteria,
        get_input()
    ))))
