# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(35))