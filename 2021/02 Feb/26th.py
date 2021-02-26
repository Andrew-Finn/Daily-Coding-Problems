# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a string, return the first recurring character in it, or null if there is no recurring character.

# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.


def first_returning_char(s):
    found = set()
    for char in s:
        if char in found:
            return char
        found.add(char)
    return False


if __name__ == '__main__':
    print(first_returning_char("acbbac"))
    assert first_returning_char("acbbac") == "b"
    print(first_returning_char("abcdef"))
    assert not first_returning_char("abcdef")