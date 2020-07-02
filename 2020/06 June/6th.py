# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Airbnb.
#
# Given an array of integers, return the largest range, inclusive, of integers that are all included in the array.
#
# For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], return (8, 12) since 8, 9, 10, 11, and 12 are all in the
# array.
#  [1, 3, 6, 8, 9, 10, 11, 12]


def longest_subset(l):
    dic = {}
    l = sorted(list(set(l)))
    dic[l[0]] = [l[0]]
    for n in l[1:]:
        if n - 1 in dic:
            dic[n] = list(dic[n - 1] + [n])
            del dic[n - 1]
        else:
            dic[n] = [n]
    lrange = max(list(dic.values()), key=len)
    return min(lrange), max(lrange)


if __name__ == '__main__':
    print(longest_subset([9, 6, 1, 3, 8, 10, 12, 11]))