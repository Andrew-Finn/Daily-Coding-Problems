# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Implement a URL shortener with the following methods:
#
#     shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
#     restore(short), which expands the shortened string into the original url. If no such shortened string exists,
#     return null.
#
# Hint: What if we enter the same URL twice?
import random
import string


class URL(object):
    url_dic = {}

    def shorten(self, link):
        if link in URL.url_dic.values():
            return next((k for k, v in URL.url_dic.items() if v == link), None)

        short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        URL.url_dic[short] = link
        return short

    def restore(self, short):
        if short in URL.url_dic:
            return URL.url_dic[short]
        return "null"


if __name__ == '__main__':
    link = URL()
    assert link.restore(link.shorten("Test")) == "Test"
    assert link.shorten("Random") == link.shorten("Random")
    assert link.restore("ReVPe7") == "null"
