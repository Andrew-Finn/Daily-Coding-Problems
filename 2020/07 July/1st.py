# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are in an infinite 2D grid where you can move in any of the 8 directions:
#
#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
#
# You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of
# steps in which you can achieve it. You start from the first point.
#
# Example:
#
# Input: [(0, 0), (1, 1), (1, 2)]
# Output: 2
#
# It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).


# Question over complicates the problem, function to get distance from A-> B moving a distance of 1 (Including diagonal)
# main can loop this for array

def grid_distance(x1, y1, x2, y2):
    distance = 0
    while x1 != x2 or y1 != y2:
        if x1 < x2:
            x1 += 1
        elif x1 > x2:
            x1 -= 1

        if y1 < y2:
            y1 += 1
        elif y1 > y2:
            y1 -= 1
        distance += 1
    return distance


def grid_points(grid_list):
    total_distance = 0
    for i in range(len(grid_list) - 1):
        total_distance += grid_distance(grid_list[i][0], grid_list[i][1], grid_list[i + 1][0], grid_list[i + 1][1])
    return total_distance


if __name__ == '__main__':
    assert grid_points([(0, 0), (1, 1), (1, 2)]) == 2
    assert grid_points([(0, 0), (1, 1), (2, 2)]) == 2
    assert grid_points([(0, 0), (1, 2), (0, 0)]) == 4
    assert grid_points([(0, 0), (-1, -1), (2, 2)]) == 4
    print(grid_points([(0, 0), (1, 1), (1, 2)]))
