# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a sorted list of integers, square the elements and give the output in sorted order.
#
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].


def square_elements(l):
    return sorted([x ** 2 for x in l])


if __name__ == '__main__':
    assert square_elements([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
    print(square_elements([-9, -2, 0, 2, 3]))