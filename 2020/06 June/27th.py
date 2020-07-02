# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Epic.
#
# The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually
# describes the digits appearing in the previous term. The first few terms are as follows:
#
# 1
# 11
# 21
# 1211
# 111221
#
# As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.
#
# Given an integer N, print the Nth term of this sequence.


def get_next(n):
    n = str(n)
    k, last, result = 1, n[0], ''
    for i in range(1, len(n)):
        if last == n[i]:
            k += 1
        else:
            result = result + str(k) + last
            k = 1
        last = n[i]
    result = result + str(k) + last
    return int(result)


def look_and_say(n):
    # Base Cases
    if n == 1:
        return 1
    elif n == 2:
        return 11

    n -= 2
    out = get_next(1)
    while n != 0:
        out = get_next(out)
        n -= 1
    return out


if __name__ == '__main__':
    print(look_and_say(5))
