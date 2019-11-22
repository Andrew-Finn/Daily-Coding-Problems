# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Airbnb.
#
# Given a linked list and a positive integer k, rotate the list to the right by k places.
#
# For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
#
# Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.


def rotate_by_n(l, n):
    if n == 0:
        return l
    return rotate_by_n(l[-1:] + l[:-1], n - 1)


if __name__ == '__main__':
    print(rotate_by_n([7, 7, 3, 5], 2))
    print(rotate_by_n([1, 2, 3, 4, 5], 3))