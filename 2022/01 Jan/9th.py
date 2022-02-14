# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Slack.
#
# You are given a string formed by concatenating several words corresponding to the integers zero through nine and
# then anagramming.
#
# For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be
# multiple instances of each integer.
#
# Given this string, return the original integers in sorted order. In the example above, this would be 357.

def unanagram_string_of_numbers(s):
    nl = [
        ["z", "zero", "0"],
        ["w", "two", "2"],
        ["u", "four", "4"],
        ["f", "five", "5"],
        ["x", "six", "6"],
        ["v", "seven", "7"],
        ["g", "eight", "8"],
        ["o", "one", "1"],
        ["n", "nine", "9"],
        ["e", "three", "3"]
    ]
    output = []
    for n in nl:
        while n[0] in s:
            for letter in n[1]:
                s = s.replace(letter, "", 1)
            output.append(n[2])
    return "".join(sorted(output))


if __name__ == '__main__':
    import random
    assert unanagram_string_of_numbers("niesevehrtfeev") == "357"
    for i in range(50):
        nl = [
            ["z", "zero", "0"],
            ["w", "two", "2"],
            ["u", "four", "4"],
            ["f", "five", "5"],
            ["x", "six", "6"],
            ["v", "seven", "7"],
            ["g", "eight", "8"],
            ["o", "one", "1"],
            ["n", "nine", "9"],
            ["e", "three", "3"]
        ]
        ans = []
        inp = ""
        for _ in range(random.randint(50, 250)):
            g = random.choice(nl)
            ans.append(g[2])
            inp += g[1]
        assert unanagram_string_of_numbers(inp) == "".join(sorted(ans))

