# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Nvidia.
#
# Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.


def get_max(x, y):
    return x ^ ((x ^ y) & -(x < y))


if __name__ == '__main__':
    import random
    n1, n2 = random.randint(0, 100000), random.randint(0, 100000)
    assert max([n1, n2]) == get_max(n1, n2)
