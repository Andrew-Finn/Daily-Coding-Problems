# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given two strings A and B, return whether or not A can be shifted some number of times to get B.
#
# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.


def shift_check(a, b):
    l = len(a)
    a = a * 2
    for i in range(len(a) - l):
        if b == a[i:i + l]:
            return True
    return False


if __name__ == '__main__':
    assert shift_check("abcde", "cdeab")
    assert not shift_check("abc", "acb")
    print(shift_check("abcde", "cdeab"))
    print(shift_check("abc", "acb"))
