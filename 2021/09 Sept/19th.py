# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Microsoft.
# 
# Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For 
# example, given the string "abracadabra" and the pattern "abr", you should return [0, 7]. 

import re


def find_starting_indices(string, to_match) -> [int]:
    return [m.start(0) for m in re.finditer(to_match, string)]


if __name__ == '__main__':
    assert find_starting_indices("abracadabra", "abr") == [0, 7]
    assert find_starting_indices("abracadabra", "abrx") == []