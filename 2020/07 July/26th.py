# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a pivot x, and a list lst, partition the list into three parts.
#
#     The first part contains all elements in lst that are less than x
#     The second part contains all elements in lst that are equal to x
#     The third part contains all elements in lst that are larger than x
#
# Ordering within a part can be arbitrary.
#
# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].


# Simple Solution, can also be done in place push greater to the end of the list, smallest to the start and pop
# original, do nothing with equal. Would run slower but have significant less memory overhead (len(l) + 1) vs (2 *
# len(l)), also pop on large data arrays is slow
def pivot_partition(pivot, l):
    i = 0
    less, equal, greater = [], [], []
    for n in l:
        if n < pivot:
            less.append(n)
        elif n == pivot:
            equal.append(n)
        else:
            greater.append(n)
    return less + equal + greater

if __name__ == '__main__':
    print(pivot_partition(3, [9, 12, 3, 5, 14, 10, 10]))
    print(pivot_partition(10, [9, 12, 3, 5, 14, 10, 10]))