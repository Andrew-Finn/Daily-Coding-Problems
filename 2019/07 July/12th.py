# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the
# matrix by going left-to-right, or up-to-down.
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]


def left_to_right(m, find):
    for line in m:
        if "".join(line) == find:
            print(True, "-", find, "found")
            return True


def up_to_down(m, find):
    for i in range(len(m[0])):
        vert = []
        for line in m:
            vert.append(line[i])
        if "".join(vert) == find:
            print(True, "-", find, "found")
            return True


def matrix_check(m, find):
    found = False
    if left_to_right(m, find):
        found = True
    elif up_to_down(m, find):
        found = True
    if not found:
        print("False - Word not found")


if __name__ == '__main__':
    print("Test 1 - No words")

    matrix_check([['F', 'A', 'C', 'I'],
                  ['O', 'B', 'Q', 'P'],
                  ['D', 'N', 'G', 'B'],
                  ['M', 'A', 'S', 'G']], "RAND")
    print("\nTest 2 - Sample 1")
    matrix_check([['F', 'A', 'C', 'I'],
                  ['O', 'B', 'Q', 'P'],
                  ['A', 'N', 'O', 'B'],
                  ['M', 'A', 'S', 'S']], "FOAM")
    print("\nTest 3 - Sample 2")
    matrix_check([['F', 'A', 'C', 'I'],
                  ['O', 'B', 'Q', 'P'],
                  ['A', 'N', 'O', 'B'],
                  ['M', 'A', 'S', 'S']], "MASS")
