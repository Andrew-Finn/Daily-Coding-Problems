# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Robinhood.
#
# Given an array of strings, group anagrams together.
#
# For example, given the following array:
#
# ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
#
# Return:
#
# [['eat', 'ate', 'tea'],
#  ['apt', 'pat'],
#  ['now']]


def group_anagrams(l):
    dic = {}
    for word in l:
        sword = ''.join(sorted(word))
        if sword not in dic:
            dic[sword] = [word]
        else:
            dic[sword] += [word]
    return list(dic.values())


if __name__ == '__main__':
    print(group_anagrams(['eat', 'ate', 'apt', 'pat', 'tea', 'now']))
