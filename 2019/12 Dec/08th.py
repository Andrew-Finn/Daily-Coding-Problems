# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Dropbox.
#
# Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ",
# "AAA", "AAB", ....
#
# Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".


def alphabetical_id(n):
    out = ""
    while n != 0:
        n, remainder = divmod(n - 1, 26)
        out = chr(65 + remainder) + out
    return out


if __name__ == '__main__':
    assert alphabetical_id(27) == "AA"
