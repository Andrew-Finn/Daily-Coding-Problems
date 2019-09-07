# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here",
# return "here world hello"


def reverse_order(s):
    return " ".join(s.split()[::-1])


if __name__ == '__main__':
    assert reverse_order("hello world here") == "here world hello"
    assert reverse_order("1 2 3 4 5 6 7 8 9") == "9 8 7 6 5 4 3 2 1"
    print(reverse_order("hello world here"))