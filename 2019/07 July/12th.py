# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given a 2D matrix of characters and a target word(#Problem changed to find all english words of max length), write a
# function that returns whether the word can be found in the
# matrix by going left-to-right, or up-to-down.
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]

import enchant


def left_to_right(m):
    printed = False
    dic = enchant.Dict("en_UK")
    for line in m:
        if dic.check("".join(line)):
            print("Word found:", "".join(line))
            printed = True
    return printed


def up_to_down(m):
    printed = False
    dic = enchant.Dict("en_UK")
    for i in range(len(m[0])):
        vert = []
        for line in m:
            vert.append(line[i])
        if dic.check("".join(vert)):
            print("Word found:", "".join(vert))
            printed = True
    return printed


def matrix_check(m):
    word_found = False
    if left_to_right(m):
        word_found = True
    if up_to_down(m):
        word_found = True
    if word_found:
        print("True : Word(s) found")
    else:
        print("No word found")


if __name__ == '__main__':
    print("Test 1 - No words")

    matrix_check([['F', 'A', 'C', 'I'],
                  ['O', 'B', 'Q', 'P'],
                  ['D', 'N', 'G', 'B'],
                  ['M', 'A', 'S', 'G']])
    print("\nTest 2 - Sample")
    matrix_check([['F', 'A', 'C', 'I'],
                  ['O', 'B', 'Q', 'P'],
                  ['A', 'N', 'O', 'B'],
                  ['M', 'A', 'S', 'S']])
