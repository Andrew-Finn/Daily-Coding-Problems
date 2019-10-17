# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by MongoDB.
#
# Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).
#
# You can assume that such element exists.
#
# For example, given [1, 2, 1, 1, 3, 4, 0], return 1.


# Invalid question ??
# In example 1 occurs 3 times, len(list) = 7 , 3 is not less than 3 -> False
# Assumption >= len(list) // 2 instead of > len(list) // 2 ... "more than or exactly half the time" ?

def find_majority_e(l):
    len_l = len(l)
    for n in l:
        if l.count(n) >= len_l // 2:
            return n
        l = [x for x in l if x != n]


if __name__ == '__main__':
    assert find_majority_e([1, 2, 1, 1, 3, 4, 0]) == 1