def get_input():
    with open("d3_input", "r") as f:
        return [
            list(line)
            for line in list(filter(
                    lambda x: x != "",
                    f.read().split("\n")
            ))
        ]

def exercise_1():
    x = 0
    y = 0
    trees = 0
    
    slope = get_input()
    width = len(slope[0])

    while y < len(slope):
        if slope[y][x % width] == '#':
            trees += 1
        x += 3
        y += 1

    print(trees)


def exercise_2():
    pairs = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    slope = get_input()
    width = len(slope[0])
    tree_product = 1

    for x_inc, y_inc in pairs:
        x = 0
        y = 0
        trees = 0

        while y < len(slope):
            print(x, y, x_inc, y_inc)
            if slope[y][x % width] == '#':
                trees += 1
            x += x_inc
            y += y_inc

        tree_product *= trees

    print(tree_product)
