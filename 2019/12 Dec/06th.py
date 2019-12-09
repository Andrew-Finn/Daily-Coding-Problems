# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
#
#     if n is even, the next number in the sequence is n / 2
#     if n is odd, the next number in the sequence is 3n + 1
#
# It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
#
# Bonus: What input n <= 1000000 gives the longest sequence?


def collatz_sequence(n):
    out = []
    while n != 1:
        out.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return out + [1]


def longest_collatz_sequence(n):
    longest = 0
    for i in range(1,n):
        curr = collatz_sequence(n)
        if len(curr) > longest:
            longest, c = len(curr), i
    return longest, i


if __name__ == '__main__':
    print(longest_collatz_sequence(1000000))