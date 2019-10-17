# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a string, determine whether any permutation of it is a palindrome.
#
# For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
# daily should return false, since there's no rearrangement that can form a palindrome.


def rearrange_palindrome(s):
    lcount = {}
    for letter in s:
        if letter in lcount:
            lcount[letter] += 1
            continue
        lcount[letter] = 1

    oddcheck = True
    for n in lcount.values():
        if n % 2 == 0:
            continue
        elif n == 1:
            if oddcheck:
                oddcheck = False
                continue
            return False
        else:
            return False
    return True


if __name__ == '__main__':
    assert rearrange_palindrome("carrace") is True
    assert rearrange_palindrome("racecar") is True
    assert rearrange_palindrome("112233") is True
    assert rearrange_palindrome("1122334") is True
    assert rearrange_palindrome("carraces") is False
    assert rearrange_palindrome("1122334456") is False
