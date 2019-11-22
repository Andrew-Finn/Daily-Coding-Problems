# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Bloomberg.
#
# Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
#
# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
#
# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.


def IsOneToOneMap(s1, s2):
    dic = {}
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] in dic:
            if dic[s1[i]] != s2[i]:
                return False
        dic[s1[i]] = s2[i]
    return True


if __name__ == '__main__':
    print(IsOneToOneMap("abc", "bcd"))
    print(IsOneToOneMap("foo", "bar"))

