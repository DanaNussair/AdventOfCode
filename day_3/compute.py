from .data import tree_map
from functools import reduce


def perform_tree_count_part_one(direction):
    rows = tree_map.split('\n')
    [right, down] = direction
    col_increase = 1
    trees = 0
    for index, row in enumerate(rows):
        if index >= direction[1]:
            col = list(row) * col_increase
            if direction[0] <= len(col) and col[direction[0]] == '#':
                trees += 1
            else:
                col_increase += 1

            direction = (direction[0] + right, index + down)
    return trees


def perform_tree_count_part_two(directions):
    count_arr = []

    for direction in directions:
        count_arr.append(perform_tree_count_part_one(direction))
    print(count_arr)
    return reduce(lambda a, b: a * b, count_arr)

print("Part One: {}".format(perform_tree_count_part_one((3, 1))))
print("Part Two: {}".format(perform_tree_count_part_two([(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)])))