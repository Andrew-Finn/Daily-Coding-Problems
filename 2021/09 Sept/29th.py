# Good morning! Here's your coding interview problem for today.
#
# Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words
# in a string.
#
# For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world",
# return 1 because there's only one word "cat" in between the two words.


def generate_dict_word_index(l):
    dict = {}
    for word_i in range(len(l)):
        word = l[word_i]
        if word in dict:
            dict[word].append(word_i)
        else:
            dict[word] = [word_i]
    return dict


def find_shortest_distance_between(content, w1, w2):
    dict = generate_dict_word_index(content.split(" "))
    if w1 not in dict or w2 not in dict:
        return False
    curr_min = float('inf')
    for w1_index in dict[w1]:
        for w2_index in dict[w2]:
            dist = abs(w1_index - w2_index) - 1
            if dist < curr_min:
                curr_min = dist
    return curr_min


if __name__ == '__main__':
    assert find_shortest_distance_between("dog cat hello cat dog dog hello cat world", "hello", "world") == 1
    assert find_shortest_distance_between("dog cat hello cat dog dog hello two cats world", "hello", "world") == 2
    assert find_shortest_distance_between("dog cat hello cat dog dog hello world", "hello", "world") == 0
    assert find_shortest_distance_between("hello hello big bad world cat dog dog hello world", "hello", "world") == 0
    assert find_shortest_distance_between("hello {}world".format("word " * 100), "hello", "world") == 100
    assert find_shortest_distance_between("hello {}world".format("hello " * 100), "hello", "world") == 0
    assert not find_shortest_distance_between("dog cat hello cat dog dog hello two cats world", "wrong", "input")


