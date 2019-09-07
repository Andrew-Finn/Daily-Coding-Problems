# This problem was asked by Cisco.
#
# Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th
# bit should be swapped, and so on.
#
# For example, 10101010 should be 01010101. 11100010 should be 11010001.
#
# Bonus: Can you do this in one line?


def bit_swap(b):
    return str(b)[1::-1] + str(b)[3:1:-1] + str(b)[5:3:-1] + str(b)[7:5:-1]


if __name__ == '__main__':
    assert str(bit_swap(10101010)) == "01010101"
    assert str(bit_swap(11100010)) == "11010001"
