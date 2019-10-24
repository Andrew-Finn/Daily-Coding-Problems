# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of integers, return a new array where each element in the new array is the number of smaller elements
# to the right of that element in the original input array.
#
# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
#
#     There is 1 smaller element to the right of 3
#     There is 1 smaller element to the right of 4
#     There are 2 smaller elements to the right of 9
#     There is 1 smaller element to the right of 6
#     There are no smaller elements to the right of 1


def smaller_left(l):
    for i in range(len(l) - 1):
        smaller = 0
        for n in l[i + 1:]:
            if l[i] > n:
                smaller += 1
        l[i] = smaller
    return l[:-1] + [0]


if __name__ == '__main__':
    assert smaller_left([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
    print(smaller_left([3, 4, 9, 6, 1]))
