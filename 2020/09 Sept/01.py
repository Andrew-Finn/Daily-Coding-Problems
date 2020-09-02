# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole
# principle, there must be a duplicate. Find it in linear time and space.
import random


def pigeon_duplicate(l):
    return (((len(l) + 1) * (len(l) + 2)) // 2) - sum(l)


if __name__ == '__main__':
    assert pigeon_duplicate([1, 2, 3, 4, 6, 7, 8, 9]) == 5
    for j in range(10000):
        m = [x for x in range(1, 10000)]
        t = m.pop(random.randint(0, len(m) - 1))
        assert pigeon_duplicate(m) == t
