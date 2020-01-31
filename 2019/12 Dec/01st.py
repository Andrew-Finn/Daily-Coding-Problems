def next_permutation(i):
    l = [int(x) for x in str(i)]
    i, j = len(l) - 1, len(l) - 1
    while i > 0 and l[i - 1] >= l[i]:
        i -= 1
    if i <= 0:
        return False

    while l[j] <= l[i - 1]:
        j -= 1
    l[i - 1], l[j] = l[j], l[i - 1]
    l[i:] = l[len(l) - 1: i - 1: -1]
    return int("".join(map(str, l)))


if __name__ == '__main__':
    print(next_permutation(48975))
