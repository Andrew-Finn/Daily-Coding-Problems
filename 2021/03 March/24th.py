# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# You are given a set of synonyms, such as (big, large) and (eat, consume). Using this set, determine if two
# sentences with the same number of words are equivalent.

# For example, the following two sentences are equivalent:

#     "He wants to eat food."
#     "He wants to consume food."

# Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c): consider the case of (coach, bus)
# and (coach, teacher).

# Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b, c)?
import string


def synonym_equivalent(sentence_a, sentence_b, synonyms, equivalence=False):
    words_a = ("".join([letter for letter in sentence_a if letter in (string.ascii_letters + " ")])).lower().split()
    words_b = ("".join([letter for letter in sentence_b if letter in (string.ascii_letters + " ")])).lower().split()

    equivalence_dict = {}
    for tupl in synonyms:
        equivalence_dict[tupl[1]] = tupl[0]
        if equivalence:
            equivalence_dict[tupl[0]] = tupl[1]

    if len(words_a) != len(words_b):
        return False

    for word_index in range(len(words_a)):
        try:
            if not (words_a[word_index] == words_b[word_index] or
                    words_a[word_index] == equivalence_dict[words_b[word_index]]):
                return False
        except KeyError:
            return False
    return True


if __name__ == '__main__':
    print(synonym_equivalent("He wants to eat food.", "He wants to consume food.", [("eat", "consume")]))
    print(synonym_equivalent("He wants to eat food.", "He wants to consume food.", [("consume", "eat")],
                             equivalence=True))
