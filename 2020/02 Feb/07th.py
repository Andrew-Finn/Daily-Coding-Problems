# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct
# elements, return a fixed point, if one exists. Otherwise, return False.
#
# For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.


def has_fixed_point(l):
    for i in range(len(l)):
        if l[i] == i:
            return i
    return False


if __name__ == '__main__':
    assert has_fixed_point([-6, 0, 2, 40]) == 2
    assert has_fixed_point([[1, 5, 7, 8]]) is False
