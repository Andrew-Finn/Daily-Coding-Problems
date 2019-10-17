# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the head of a singly linked list, swap every two nodes and return its head.
#
# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.


def swap_nodes(l):
    i = 0
    while i < len(l) - 1:
        tmp = l[i + 1]
        l[i + 1] = l[i]
        l[i] = tmp
        i += 2
    return l


if __name__ == '__main__':
    print(swap_nodes(list(range(25))))
    assert swap_nodes([1, 2, 3, 4]) == [2, 1, 4, 3]