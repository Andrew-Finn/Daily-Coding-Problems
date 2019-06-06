# This problem was asked by Facebook.
#
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced
# (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false.
import sys


def is_matched(expression):
    mapping = dict(zip('({[', ')}]'))
    queue = []
    for letter in expression:
        if letter in mapping:
            queue.append(mapping[letter])
        elif letter not in mapping.values():
            return "False : {} not in mapping".format(letter)
        elif not (queue and letter == queue.pop()):
            return False
    return not queue


if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        if len(line) != 0:
            print(is_matched(line))
