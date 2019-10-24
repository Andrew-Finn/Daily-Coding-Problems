# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a 32-bit integer, return the number with its bits reversed.
#
# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
# return 0000 1111 0000 1111 0000 1111 0000 1111.


def binary_reverse(bits):
    out = ""
    for i in str(bits):
        if i == "1":
            out += "0"
        elif i == "0":
            out += "1"
        else:
            out += " "
    return out


if __name__ == '__main__':
    assert binary_reverse("1111 0000 1111 0000 1111 0000 1111 0000") == "0000 1111 0000 1111 0000 1111 0000 1111"
    print(binary_reverse("1111 0000 1111 0000 1111 0000 1111 0000"))