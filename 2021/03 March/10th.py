# Good morning! Here's your coding interview problem for today.

# This problem was asked by Netflix.

# Given a sorted list of integers of length N, determine if an element x is in the list without performing any
# multiplication, division, or bit-shift operations.

# Do this in O(log N) time.


def binary_search(l, s):
    if len(l) == 1:
        return True if l[0] == s else False
    elif l[len(l) // 2] == s:
        return True
    elif l[len(l) // 2] < s:
        return binary_search((l[len(l) // 2:]), s)
    return binary_search((l[:len(l) // 2]), s)


if __name__ == "__main__":
    import random

    for i in range(500):
        l = sorted([random.randint(1, 999) for x in range(99)])
        for i in range(10):
            s = random.choice(l)
            assert binary_search(l, s) == True

        for _ in range(10):
            while True:
                n = random.randint(1, 999)
                if n not in l:
                    assert binary_search(l, n) == False
                    break
