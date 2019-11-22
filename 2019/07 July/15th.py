# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Square.
#
# Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also
# not 0-100 or 100-0). You do not know the bias of the coin.
#
# Write a function to simulate an unbiased coin toss.

import random

ranprob = random.randint(1, 99)
print("toss_biased probability: {}:{}".format(ranprob, 100 - ranprob))


def toss_biased():
    n = random.randint(1, 99)
    if n <= ranprob:
        return "Heads"
    return "Tails"


def unbiased_toss():
    while True:
        r1, r2 = toss_biased(), toss_biased()
        if r1 != r2:
            return r1


if __name__ == '__main__':
    heads = 0
    rounds = 100000
    for i in range(rounds):
        if unbiased_toss() == "Heads":
            heads += 1
    print("Heads: {:2f}%\nTails: {:2f}%".format((rounds - heads) / rounds * 100, heads / rounds * 100))
