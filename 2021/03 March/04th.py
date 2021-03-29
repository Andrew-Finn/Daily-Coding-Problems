# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a 32-bit integer, return the number with its bits reversed.

# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.

def flip_binary(n):
    return "".join(["1" if x == "0" else "0" if x == "1" else x for x in n])

if __name__ == '__main__':
    assert flip_binary("1111 0000 1111 0000 1111 0000 1111 0000") == "0000 1111 0000 1111 0000 1111 0000 1111"
