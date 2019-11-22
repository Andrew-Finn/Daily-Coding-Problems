# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given n numbers, find the greatest common denominator between them.
#
# For example, given the numbers [42, 56, 14], return 14.

# Method 1 ---> Blatant 'cheating'

from fractions import gcd


def gcdl(l):
    result = l[0]
    for i in l[1:]:
        result = gcd(result, i)
    return result


if __name__ == '__main__':
    print(gcdl([42, 56, 14]))