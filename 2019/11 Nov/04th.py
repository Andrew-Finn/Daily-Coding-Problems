# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple
# probabilistic games.
#
# The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is
# the amount you pay, in dollars.
#
# The second game: same, except that the stopping condition is a five followed by a five.
#
# Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games
# and calculate their expected value.

# TLDR: It doesnt matter what game is picked the probability of the next number(N) being X is not affected by number
# N - 1

import random


def game_one():
    r1, r2 = random.randint(1, 6), random.randint(1, 6)
    i = 2
    while r1 != 5 and r2 != 6:
        r2 = r1
        r1 = random.randint(1, 6)
        i += 1
    return i


def game_two():
    r1, r2 = random.randint(1,6), random.randint(1,6)
    i = 2
    while r1 != r2 and r1 != 5:
        r2 = r1
        r1 = random.randint(1, 6)
        i += 1
    return i


if __name__ == '__main__':
    g1, g2 = [0, 0]
    for i in range(100000):
        g1 += game_one()
        g2 += game_two()
    print("Average cost over 100,000 iterations:\nGame One: ${}\nGame Two: ${}".format(g1 / 100000, g2 / 100000))
