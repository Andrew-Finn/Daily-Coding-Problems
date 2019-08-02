# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# A number is considered perfect if its digits sum up to exactly 10.
#
# Given a positive integer n, return the n-th perfect number.
#
# For example, given 1, you should return 19. Given 2, you should return 28.


def find_nth_perfect(n):
    count = 0
    curr = 0
    while True:
        sum = 0
        x = curr
        while x:
            sum += x % 10
            x = x // 10

        if sum == 10:
            count = count + 1

        if count == n:
            return curr
        curr += 1


if __name__ == '__main__':
    print(find_nth_perfect(100))