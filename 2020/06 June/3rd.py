# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# You are given an unsorted list of 999,000 unique integers, each from 1 and 1,000,000. Find the missing 1000
# numbers. What is the computational and space complexity of your solution?

import random


def find_missing(l):
    dic = {n: None for n in range(1000000)}
    for n in l[::-1]:
        if n in dic:
            del dic[n]
        del l[::-1]
    return list(dic.keys())


if __name__ == '__main__':
    print("Generating test list ....", end="")
    l = [x for x in range(1000000)]
    popped = []
    for i in range(1000):
        n = random.randint(0, len(l))
        n = l.pop(n)
        popped.append(n)
    print("Done\nFinding mising...")
    out = find_missing(l)
    print(out)
    assert set(out) == set(popped)

