# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
#
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
#
# You can assume the list has at least three integers.


def max_sum(l):
    l = sorted(l)
    out = [l[0] * l[1] * l[-1], l[-1] * l[-2] * l[-3]]  # More efficient ways but this is the simplest
    return max(out)


if __name__ == '__main__':
    print(max_sum([-10, -10, 5, 2]))
    print(max_sum([10, -10, 5, 2]))
    print(max_sum([-10, -10, -5, -2]))
    print(max_sum([1, 3, -5, -10]))