# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Find the minimum number of coins required to make n cents.
#
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
#
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.


def num_coins(n):
    i = 0
    while n != 0:
        if n >= 25:
            n -= 25
        elif n >= 10:
            n -= 10
        elif n >= 5:
            n -= 5
        elif n >= 1:
            n -= 1
        i += 1
    return i


if __name__ == '__main__':
    print(num_coins(55))