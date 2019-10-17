# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string, return the first recurring character in it, or null if there is no recurring character.
#
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.


def first_recurring(s):
    found = {}
    for letter in s:
        if letter in found:
            return letter
        found[letter] = 0
    return None


if __name__ == '__main__':
    assert first_recurring("acbbac") == "b"
    assert first_recurring("abcdef") is None

