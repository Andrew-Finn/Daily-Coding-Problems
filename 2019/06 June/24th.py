# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a
# function rand7() that returns an integer from 1 to 7 (inclusive).

import secrets
# Secrets acts similarly to random module however secrets is cryptographically .


def rand5():
    return secrets.choice(range(1, 6))


def rand7():
    return secrets.choice(range(1, 8))


if __name__ == '__main__':
    print(rand5())
    print(rand7())
