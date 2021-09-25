# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Nest.
#
# Create a basic sentence checker that takes in a stream of characters and determines whether they form valid
# sentences. If a sentence is valid, the program should print it out.
#
# We can consider a sentence valid if it conforms to the following rules:
#
#     The sentence must start with a capital letter, followed by a lowercase letter or a space.
#     All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
#     There must be a single space between each word.
#     The sentence must end with a terminal mark immediately following a word.

import re
import string


def is_valid_sentence_ending(sentence) -> bool:
    if re.match(r'[a-zA-Z]+[.?!‽]', sentence.split(" ")[-1]):
        return True
    return False


def is_valid_sentence_start(sentence) -> bool:
    if len(sentence) < 2:
        return False
    if sentence[0] in string.ascii_uppercase and sentence[1] in string.ascii_lowercase + " ":
        return True
    return False


def contains_only_valid_characters(sentence):
    return not bool([x for x in sentence[1:] if x not in string.ascii_lowercase + ",;:.?!‽ "])


def contains_no_double_space(sentence):
    return not "  " in sentence


def is_valid_sentence(sentence) -> bool:
    return is_valid_sentence_ending(sentence) \
           and is_valid_sentence_start(sentence) \
           and contains_only_valid_characters(sentence) \
           and contains_no_double_space(sentence)


if __name__ == '__main__':
    assert is_valid_sentence("String that is a valid sentence.")
    assert is_valid_sentence("This is also a valid sentence.")
    assert is_valid_sentence("So is this!")
    assert not is_valid_sentence("This missing a full stop at the end")
    assert not is_valid_sentence("this starts with a small letter")
    assert not is_valid_sentence("This  has  two  spaces")
    assert not is_valid_sentence("This has invalid characters :).")



