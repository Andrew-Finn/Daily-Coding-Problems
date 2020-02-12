# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Netflix.
#
# Given a sorted list of integers of length N, determine if an element x is in the list without performing any
# multiplication, division, or bit-shift operations.
#
# Do this in O(log N) time.

import random


def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


if __name__ == '__main__':
    assert binary_search([1, 2, 3, 4, 5], 7) is False
    assert binary_search([1, 2, 3, 4, 5], 2) is True
    for i in range(1000):
        i, l = random.randint(1, 999), [x for x in range(1000)]
        assert binary_search(l, i) is True
        assert binary_search([x for x in l if x != i], i) is False
