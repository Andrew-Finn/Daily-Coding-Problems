# Good morning! Here's your coding interview problem for today.
#
# This question was asked by ContextLogic.
#
# Implement division of two positive integers without using the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder.
import random


def useless_divide(x, divisor):
    answer, curr = 0, 0
    while True:
        if curr + divisor <= x:
            curr += divisor
            answer += 1
            continue
        return answer


if __name__ == '__main__':
    for i in range(1000):
        r1 = random.randrange(5, 1000000)
        r2 = random.randrange(2, r1 - 1)
        print("{} // {} = {}".format(r1, r2, r1 // r2))
        assert useless_divide(r1, r2) == r1 // r2
