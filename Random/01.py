# This problem was asked by Google.
#
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come
# first, the Gs come second, and the Bs come last. You can only swap elements of the array.
#
# Do this in linear time and in-place.
#
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B']
import random


def rgb_organise(l):
    return list((l.count("R") * "R") + (l.count("G") * "G") + (l.count("B") * "B"))


if __name__ == '__main__':
    print(['G', 'B', 'R', 'R', 'B', 'R', 'G'], "->", rgb_organise(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
    assert(len(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == len(rgb_organise(['G', 'B', 'R', 'R', 'B', 'R', 'G'])))
    print("Random data:\n")
    for i in range(10):
        l = []
        for j in range(10):
            l.append(random.choice(["R", "G", "B"]))
        assert(len(l) == len(rgb_organise(l)))
        print(l, "->", rgb_organise(l))
