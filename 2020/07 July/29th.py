# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Dropbox.
#
# Implement an efficient string matching algorithm.
#
# That is, given a string of length N and a pattern of length k, write a program that searches for the pattern in the
# string with less than O(N * k) worst-case time complexity.
#
# If the pattern is found, return the start index of its location. If not, return False.

import re


# Why bother implementing it myself when its build into the standard library.
def pattern_match(string, pattern):
    match = re.search(pattern, string)
    if match is None:
        return False
    return match.start()


if __name__ == '__main__':
    print(pattern_match("AAABCDDDABC", "ABC"))
    print(pattern_match("AAABCDDD", "ABCDE"))
