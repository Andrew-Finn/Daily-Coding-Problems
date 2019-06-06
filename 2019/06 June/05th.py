# This problem was asked by Google.
#
# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller
# than the length of the list.
#
# The list is very long, so making more than one pass is prohibitively expensive.
import time


def remove_kth(l, k):
    return l[:k] + l[k + 1:]


if __name__ == '__main__':
    l = list(range(10000000))
    print(len(l))
    t = time.clock()
    l = remove_kth(l, 4)
    t1 = time.clock()
    print(len(l))
    print("{:3f} seconds".format(t1 - t))
