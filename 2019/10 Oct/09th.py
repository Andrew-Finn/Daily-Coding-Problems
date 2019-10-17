# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Triplebyte.
#
# You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers
# with its corresponding probability.
#
# For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1
# 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.
#
# You can generate random numbers between 0 and 1 uniformly.
import random


def rand_element(l, prob):
    prob_list, t = [], 100
    for e in prob:
        prob_list.append(int(t - (e * 100)))
        t -= e * 100
    randint = random.randint(0, 99)
    for i in range(len(prob_list)):
        if randint >= prob_list[i]:
            return l[i]


if __name__ == '__main__':
    # Must be ran in terminal Unix base only.
    import os
    d, i = {1: 0, 2: 0, 3: 0, 4: 0}, 1
    while True:
        d[rand_element([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])] += 1
        if i % 100000 == 0:
            os.system("clear")  # Linux and OSX only
            print("Ctrl + C to force stop program")
            print("Current iterations: {:,d} (Table updates every 100,000 intervals)".format(i))
            print("1 occurred {:.4f}% of the time (Goal was 10%),\n2 occurred {:.4f}% of the time (Goal was 50%),\n"
                  "3 occurred {:.4f}% of the time (Goal was 20%),\n4 occurred {:.4f}% of the time (Goal was 20%).\n".
                  format(d[1] / i * 100, d[2] / i * 100, d[3] / i * 100, d[4] / i * 100))
        i += 1
