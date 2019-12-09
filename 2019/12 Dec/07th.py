# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For
# example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].


def start_index(s, m):
    if not m or not s or len(m) > len(s): # Edge cases
        return None
    if s == m:
        return [0]
    out = []
    for i in range(len(s) - len(m)):
        if s[i:i + len(m)] == m:
            out.append(i)
    return out


if __name__ == '__main__':
    print(start_index("abracadabra", "abr"))