# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle,
# there must be a duplicate. Find it in linear time and space.


def find_duplicate(l):
    return sum(l) - (((l[-1] ** 2) + l[-1]) // 2)


if __name__ == '__main__':
    import random
    assert find_duplicate(sorted(list(range(100)) + [50])) == 50
    ran1 = random.randint(100, 100000)
    ran2 = random.randint(1, ran1 - 1)
    print("Length of list =", ran1, "Random duplicate =", ran2, "find_duplicate =",
          find_duplicate((sorted(list(range(ran1)) + [ran2]))))
    assert find_duplicate(sorted(list(range(ran1)) + [ran2])) == ran2
