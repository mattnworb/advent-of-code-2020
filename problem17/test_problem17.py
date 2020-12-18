from problem17 import *


ex1 = """
.#.
..#
###
"""


def test_part1_example():
    assert part1(ex1) == 112


def test_neighbors():
    ns = set(neighbors3((1, 2, 3)))

    assert len(ns) == 26
    assert ns == {
        (0, 1, 2),
        (0, 1, 3),
        (0, 1, 4),
        (0, 2, 2),
        (0, 2, 3),
        (0, 2, 4),
        (0, 3, 2),
        (0, 3, 3),
        (0, 3, 4),
        (1, 1, 2),
        (1, 1, 3),
        (1, 1, 4),
        (1, 2, 2),
        (1, 2, 4),
        (1, 3, 2),
        (1, 3, 3),
        (1, 3, 4),
        (2, 1, 2),
        (2, 1, 3),
        (2, 1, 4),
        (2, 2, 2),
        (2, 2, 3),
        (2, 2, 4),
        (2, 3, 2),
        (2, 3, 3),
        (2, 3, 4),
    }


def test_part2_example():
    assert part2(ex1) == 848