# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string, split it into as few strings as possible such that each string is a palindrome.
#
# For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].
#
# Given the input string abc, return ["a", "b", "c"].


def string_palindrome(s):
    if len(s) == 0:
        return []
    i, lrg = 0, 0
    while i < len(s):
        if s[:i + 1] == s[i::-1]:
            lrg = i + 1
        i += 1
    return [s[:lrg]] + string_palindrome(s[lrg:])


if __name__ == '__main__':
    assert string_palindrome("racecarannakayak") == ["racecar", "anna", "kayak"]
    assert string_palindrome("abc") == ["a", "b", "c"]
