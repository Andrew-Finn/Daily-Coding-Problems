# This question was asked by Google.
#
# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that
# isn't in l (uniform).

import secrets


def random_exclude(n, l):
    return secrets.choice([x for x in range(n) if x not in l])


if __name__ == '__main__':
    assert random_exclude(3, [0, 2]) == 1
    assert random_exclude(1000, list(range(999))) == 999
    assert random_exclude(10, [0, 1, 2, 3, 4, 6, 7, 8, 9]) == 5

