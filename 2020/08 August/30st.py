# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Find the minimum number of coins required to make n cents.
#
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
#
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.

def get_minimum_coins(n):
    coins = [25, 10, 5, 1]
    c = 0
    while n > 0:
        for coin in coins:
            if n - coin >= 0:
                n -= coin
                c += 1
                break
    return c


if __name__ == '__main__':
    assert get_minimum_coins(16) == 3
    print(get_minimum_coins(16))
