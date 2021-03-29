# Good morning! Here's your coding interview problem for today.

# This problem was asked by LinkedIn.

# Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2,
# return [(0, 0), (3, 1)].
from heapq import nsmallest


def get_n_nearest(points_list, central_point, n):
    distance_dic = {point: distance_ab(point, central_point) for point in points_list}
    return nsmallest(n, distance_dic, key=distance_dic.get)


def distance_ab(point_a, point_b):
    x1, y1, x2, y2 = point_a[0], point_a[1], point_b[0], point_b[1]
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** .5


if __name__ == '__main__':
    print(get_n_nearest([(0, 0), (5, 4), (3, 1)], (1, 2), 2))
    assert get_n_nearest([(0, 0), (5, 4), (3, 1)], (1, 2), 2) == [(0, 0), (3, 1)]

    import random

    print(get_n_nearest([(random.randint(-10000, 10000), random.randint(-10000, 10000)) for _ in range(100000)],
                        (0, 0), 25))
