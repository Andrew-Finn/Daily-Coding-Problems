# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# You are given an array of length 24, where each element represents the number of new subscribers during the
# corresponding hour. Implement a data structure that efficiently supports the following:
#
#     update(hour: int, value: int): Increment the element at index hour by value.
#     query(start: int, end: int): Retrieve the number of subscribers that have signed up between start and end
#     (inclusive).
#
# You can assume that all values get cleared at the end of the day, and that you will not be asked for start and end
# values that wrap around midnight.

# Assuming inclusive between


class Subscribers():
    def __init__(self, sub_list):
        self.sub_list = sub_list

    def update(self, hour, value):
        self.sub_list[hour] = self.sub_list[hour] + value
        return self.sub_list[hour]

    def query(self, start, end):
        if start == 0:
            start += 1
        return sum(self.sub_list[start - 1:end])

